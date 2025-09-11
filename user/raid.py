
from bot.database import cli

collection = cli["bot"]["raid"]


async def raid_user(chat):
    doc = {"_id": "raid", "users": [chat]}
    r = await collection.find_one({"_id": "raid"})
    if r:
        await collection.update_one({"_id": "raid"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_raid_users():
    results = await collection.find_one({"_id": "raid"})
    if results:
        return results["users"]
    else:
        return []


async def unrraid_user(chat):
    await collection.update_one({"_id": "raid"}, {"$pull": {"users": chat}})
