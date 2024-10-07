# scripts/main.py

# import tweepy
# import openai
# import yaml
# import os
# os.chdir('/Users/ashrithreddy/Documents/TechTributes')
from poem_generator import generate_poem
from post_tweet import post_tweet

def main():
    prompt = "write a poem about Elon Musk and his contribution to tech world"
    poem = generate_poem(prompt)
    poem = f'{poem} \n\n@elonmusk'
    print(poem)

    if poem:
        # post_tweet(poem)
        send_email(subject = "TechTributes", body = poem)
        print("Tweet posted successfully!")
    else:
        print("Failed to generate a poem.")

if __name__ == "__main__":
    main()


