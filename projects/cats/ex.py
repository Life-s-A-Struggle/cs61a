def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:[['What'], ['great', 'luck']]
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    result = [[] for player in player_indices]
    for w in word_indices:
        # # find the fastest in the word loop
        # fastest = min(time(game, player, w) for player in player_indices)
        # result[fastest].append(word_at(game, w)) 

        fastest = min(time(game, player, w) for player in player_indices) 
        for p in player_indices:
            if abs(time(game, p, w) - fastest) < 0.00001:
                result[p].append(word_at(game, w))

    return result
p0 = [5, 1, 3]
p1 = [4, 1, 6]
words = ['Just', 'have', 'fun']
t = [p0, p1]
fastest_words(game(words,t))

def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])