#!/usr/bin/env python3
import asyncio
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ViewerCountUpdateEvent, LikeEvent, CommentEvent
from datetime import datetime

class LiveMonitor:
    def __init__(self, username: str):
        self.client = TikTokLiveClient(f"@{username}")
        # ... (کۆدی تەواو لە وەڵامی پێشووەوە)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Session stopped!")
