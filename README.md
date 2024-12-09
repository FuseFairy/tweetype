# tweetype
Reverse Engineered Twitter Frontend API.

## Difference from Original tweety-ns:
While tweety-ns is a great tool for scraping Twitter data, this fork introduces a key change: replacing [python-magic](https://github.com/ahupp/python-magic) with [filetype](https://github.com/h2non/filetype.py) for better file type detection.

## Installation: 
```bash
pip install https://github.com/FuseFairy/tweetype/archive/main.zip --upgrade 
```

## A Quick Example:
```python
    from tweety import TwitterAsync
    import asyncio
    
    async def main():
    
        app = TwitterAsync("session")  
        all_tweets = await app.get_tweets("elonmusk")
        for tweet in all_tweets:
            print(tweet)

    asyncio.run(main())
```

> [!IMPORTANT] 
> Even Twitter Web Client has a lot of rate limits now, Abusing tweety can lead to `read_only` Twitter account.

Do check [FAQs](https://github.com/mahrtayyab/tweety/wiki/FAQs)

Full Documentation and Changelogs are [here](https://mahrtayyab.github.io/tweety_docs/)
