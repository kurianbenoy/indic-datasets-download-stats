import sys
from huggingface_hub import list_datasets


def get_downloads_for_author(author):
    """Gets total downloads for all datasets from an author."""
    total_downloads = 0
    print(f"Fetching datasets for author: {author}")
    try:
        datasets = list_datasets(
            author=author, sort="downloads", direction=-1
        )
        for ds in datasets:
            print(f"- {ds.id}: {ds.downloads} downloads")
            if ds.downloads:
                total_downloads += ds.downloads
        
        print(f"\nTotal downloads for {author}: {total_downloads}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        author_name = sys.argv[1]
        get_downloads_for_author(author_name)
    else:
        print("Usage: python download.py <author_name>")
        print("For example: python download.py huggingface")
