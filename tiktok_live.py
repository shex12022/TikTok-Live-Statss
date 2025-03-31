#!/usr/bin/env python3
import asyncio
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ViewerCountUpdateEvent, LikeEvent, CommentEvent
from datetime import datetime

class LiveReporter:
    def __init__(self, username: str):
        # ✅ ڕاستکراوی Import
        self.client = TikTokLiveClient(f"@{username}")
        self.start_time = datetime.now()
        self.stats = {
            "max_viewers": 0,
            "likes": 0,
            "comments": 0,
            "current_viewers": 0
        }

        # 🔄 ڕێگەگرتنە ڕاستەکان
        self.client.on("viewer_count_update")(self.update_viewers)
        self.client.on("like")(self.add_like)
        self.client.on("comment")(self.add_comment)

    async def start(self):
        try:
            await self.client.start()
            print(f"\n✅ پەیوەندی بە لایڤی @{username}ـەوە سازکرا!")
        except Exception as e:
            print(f"\n❌ هەڵە: {str(e)}")

    def update_viewers(self, event: ViewerCountUpdateEvent):
        self.stats["current_viewers"] = event.viewer_count
        self.stats["max_viewers"] = max(self.stats["max_viewers"], event.viewer_count)

    def add_like(self, event: LikeEvent):
        self.stats["likes"] += event.like_count

    def add_comment(self, event: CommentEvent):
        self.stats["comments"] += 1

    def show_report(self):
        duration = datetime.now() - self.start_time
        print(f"\n📊 ڕیپۆرت لە {datetime.now().strftime('%H:%M:%S')}")
        print(f"👁️ بینەر: {self.stats['current_viewers']} | ❤️ لایک: {self.stats['likes']}")
        print(f"💬 کۆمێنت: {self.stats['comments']} | 🏆 زۆرترین: {self.stats['max_viewers']}")
        print(f"⏳ ماوە: {duration}\n{'━'*40}")

async def main():
    url = input("\n🌐 لینکی لایڤەکە بنووسە: ").strip()
    username = url.split("/")[3].replace("@", "") 
    
    reporter = LiveReporter(username)
    await reporter.start()
    
    while True:
        await asyncio.sleep(3)
        reporter.show_report()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️ کۆتایی هات!")
