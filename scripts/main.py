# scripts/main.py

from utils.poem_generator import generate_poem
from scripts.post_tweet import post_tweet

def main():
    prompt = "write a poem about Elon Musk and his contribution to tech world"
    poem = generate_poem(prompt)

    if poem:
        post_tweet(poem)
        print("Tweet posted successfully!")
    else:
        print("Failed to generate a poem.")

if __name__ == "__main__":
    main()


