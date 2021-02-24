# A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the
# cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and
# the original top card is still on top.
# For example, faro shuffling the list
# ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a number
# of faro shuffles that have to be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number


line = input().split()
tours = int(input())
middle = int(len(line) / 2)

for tour in range(tours):
    first = line[:middle]
    second = line[middle:]
    cnt = 0
    for i in range(0, len(line), 2):
        line[i] = first[cnt]
        line[i + 1] = second[cnt]
        cnt += 1

print(line)


