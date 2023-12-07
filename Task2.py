import requests
import json


def download_subreddit_comments(subreddit, output_file):
    base_url = "https://api.pushshift.io/reddit/comment/search/"

    params = {
        'subreddit': subreddit,
        'sort': 'desc',  # Sorting in descending order (most recent first)
        'size': 100  # Number of comments per request, you can adjust as needed
    }

    all_comments = []

    try:
        while True:
            response = requests.get(base_url, params=params)
            response.raise_for_status()

            data = response.json()
            comments = data.get('data', [])

            if not comments:
                break  # No more comments

            all_comments.extend(comments)

            # Set the timestamp for the next request to the oldest comment in the current batch
            params['before'] = comments[-1]['created_utc']

    except requests.exceptions.RequestException as e:
        print(f"Error downloading comments: {e}")

    # Store all comments in chronological order in a JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(all_comments, file, ensure_ascii=False, indent=2)

    print(f"All comments downloaded and stored in {output_file}.")


# Example usage:
download_subreddit_comments("python", "python_subreddit_comments.json")
