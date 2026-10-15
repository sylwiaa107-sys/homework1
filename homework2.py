# 0.1. IC2.1 -- Inventory Reconciliation
# Symbol | — łączy oba zbiory nazw, bez duplikatów.
# set() — tworzy zbiór unikalnych elementów.
# .keys() służy do pobierania kluczy słownika
# .get zwraca liczbę sztuk
from enum import nonmember
from unittest import result

# from collections import Counter
# from unittest import result
#
# worker_a = ["bolt", "nut", "nut", "screw", "washer", "bolt",
# "bolt"]
# worker_b = ["bolt", "bolt", "nut", "screw", "screw", "washer"]
#
# count_a = Counter(worker_a)
# count_b = Counter(worker_b)
#
# all_items = count_a.keys() | count_b.keys()
# result = {}
#
# for item in all_items:
#     a = count_a.get(item, 0)
#     b = count_b.get(item, 0)
#     diff = a - b
#
#     result[item] = {
#         "a": a,
#         "b": b,
#         "diff": diff,
#     }
# print(result)

#0.1. IC2.3 -- Word Co-occurrence
#set - usuwa powtorzenia
#print(len(list(pairs)))

# from itertools import combinations
#
# sentences = [
#     "the cat sat on the mat",
#     "the dog chased the cat",
#     "the dog and the cat are friends",
# ]
# pair_counts = {}
# for sentence in sentences:
#     words = set(sentence.split())
#     pairs = combinations(words, 2)
#
#     for pair in pairs:
#         pair = tuple(sorted(pair))
#
#         if pair in pair_counts:
#             pair_counts[pair] += 1
#
#         else:
#             pair_counts[pair] = 1
#
# print(pair_counts)
# print(sentences)



# 0.1. IC2.4 -- Top-K with Ties
# .append() dodaje element do istniejącej listy
# reverse=True - sortuje od najwiekszego do najmniejszego

# scores = {
#     "a" : 90,
#     "b" : 85,
#     "c" : 90,
#     "d" : 70,
#     "e" : 85,
#     "f" : 60
# }
#
# def top_k_with_ties(scores, k):
#     unique_scored = sorted(set(scores.values()), reverse=True)
#     top_score = unique_scored[k - 1]
#     result = []
#
#     for name, score in scores.items():
#         if score >= top_score:
#             result.append(name)
#
#     return result
# print(top_k_with_ties(scores, 2))

#0.1. IC2.5 -- Group Transactions Into Sessions

# clicks = [1000, 1200, 1500, 5000, 5100, 5200, 10000]
# sessions = []
# current_session = []
# previous_click = None
#
# for click in clicks:
#     if previous_click is None:
#         current_session.append(click)
#     else:
#         gap = click - previous_click
#         if gap > 1800:
#             sessions.append(current_session)
#             current_session = []
#         current_session.append(click)
#     previous_click = click
#
# sessions.append(current_session)
#
# print(sessions)
#

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for word in words:
    key = tuple(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)

print(list(groups.values()))


