import os

OUTPUT_PATH = "/output/entry.txt"

SUMMARY_PART_1 = """War, diplomacy, climate and housing defined Wednesday, November 11.

In Abu Dhabi, Ukraine, Russia and the United States ended two days of talks with agreement in principle on a large prisoner-of-war exchange, but no ceasefire or territorial deal. The war went on: a Russian strike on a market in Chornomorsk killed three people and wounded 11.

In the Gulf, Iran's Revolutionary Guard said another tanker struck a mine and caught fire in the eastern Strait of Hormuz. Saudi air defences intercepted Houthi missiles and drones aimed at the Riyadh region, and Brent crude settled at $92.76 a barrel, up 1.39%. In Gaza, local health officials said Israeli strikes killed at least seven people, including a father and his 13-year-old son. Aid groups said the season's first big storm flooded about 70,000 tents and left 761,000 displaced people at risk of more flooding."""

SUMMARY_PART_2 = """

At COP31 in Antalya, UN Secretary-General Antonio Guterres told leaders from nearly 200 countries that the slow climate response had put the world on 'a path to mutually assured destruction.' Turkey pushed an electrification-centred deal, while leaders warned wars and trade disputes must not distract from climate action.

Spain staged its first general strike in 14 years. Called by the UGT and CCOO unions with tenants' groups, it targeted a housing shortage of about 750,000 homes; average rent, 1,176 euros, nearly equals a young worker's monthly salary. The strike came 18 days before the November 29 snap election.

China's trade surplus reached $1.04 trillion in January-October, a second straight year above $1 trillion, powered by AI-linked exports. In the United States, markets fully priced a 25-basis-point Federal Reserve rate hike in December after October inflation ran hot: CPI rose 0.4% and core CPI 0.3%."""

SUMMARY = SUMMARY_PART_1 + SUMMARY_PART_2


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(SUMMARY)


if __name__ == "__main__":
    main()
