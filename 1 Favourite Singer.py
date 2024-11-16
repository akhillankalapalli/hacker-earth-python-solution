def favoriteSinger(n, songs):
    singer_counts = {}
    max_count = 0
    for singer in songs:
        singer_counts[singer] = singer_counts.get(singer, 0) + 1
        max_count = max(max_count, singer_counts[singer])

    favorite_singers = 0
    for singer, count in singer_counts.items():
        if count == max_count:
            favorite_singers += 1

    return favorite_singers

n = int(input())
songs = list(map(int, input().split()))

print(favoriteSinger(n, songs))