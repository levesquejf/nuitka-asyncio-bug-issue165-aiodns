import aiodns
import asyncio


async def query(host, query_type, resolver):
    try:
        await resolver.query(host, query_type)
    except Exception as e:
        print(f"Exception: {e}")


async def run():
    loop = asyncio.get_event_loop()

    resolver = aiodns.DNSResolver(loop=loop)

    hosts = ("invalid1", "invalid2")
    for host in hosts:
        await query(host, "A", resolver)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == "__main__":
    main()
