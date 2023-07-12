import sys
import argparse
import json
import pandas as pd
from typing import List
from youtubesearchpython import VideosSearch
from pytube import YouTube
import whisper


def get_youtube_video_ids(keyword: str, limit: int = 1) -> List[str]:
    video_search = VideosSearch(keyword, limit=limit)
    results = video_search.result()['result']
    return [r['link'] for r in results]


def read_links_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()


def parse_arguments():
    parser = argparse.ArgumentParser(description='YouTube Transcription Downloader')
    parser.add_argument('-l', '--links', help='Path to the links file')
    parser.add_argument('-k', '--keyword', help='Keyword to search for on YouTube')
    parser.add_argument('-n', '--limit', type=int, default=1, help='Number of search results (default: 1)')
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.links:
        links = read_links_from_file(args.links)
    elif args.keyword:
        links = get_youtube_video_ids(args.keyword, args.limit)
    else:
        print("Please provide either --links or --keyword option.")
        return

    whisper_model = whisper.load_model("small.en")
    all_t = []
    for i in links:
        video_url = i
        v_id = video_url[len(video_url)-11:len(video_url)]
        audio_file = YouTube(video_url).streams.filter(only_audio=True).first().download(filename="audio.mp4")
        transcription = whisper_model.transcribe(audio_file)
        for i in transcription['segments']:
            i['v_id'] = v_id
        df = pd.DataFrame(data=transcription['segments'], columns=['v_id', 'start', 'end', 'text'])
        dfd = df.to_dict(orient='records')
        for d in dfd:
            all_t.append(d)
    with open('transcriptions.txt', 'w') as f:
        json.dump(all_t, f)


if __name__ == '__main__':
    main()
