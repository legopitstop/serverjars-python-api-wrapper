import serverjars


def test(type, category):
    latest = serverjars.fetch_latest(type, category)
    print(category, "-", latest.version, "-", latest.size)


test("vanilla", "release")
test("vanilla", "snapshot")
test("modded", "banner")
test("modded", "fabric")
test("modded", "mohist")
