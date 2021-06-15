from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    (AKnave and not(AKnight and AKnave)) or (AKnight and (AKnight and AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    (AKnave and not(AKnave and BKnave)) or (AKnight and (AKnave and BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is Knight and say true (both Knight or both knave OR A is Knave and say not true (both knight or both knave is not true)
    And(AKnight and ((AKnight and BKnight) or (AKnave and BKnave))) or (AKnave and (not(AKnight and BKnight) or not(AKnave and BKnave))),
    And(BKnight and ((AKnave and BKnight) or (AKnight and BKnave)) or (BKnave and (not(AKnave and BKnight) or not (AKnight and BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    (((AKnight and AKnight) or (AKnave and not AKnight)) or ((AKnight and AKnave ) or (AKnave and not AKnave))),

    ((BKnight and ((AKnight and AKnave) or (AKnave and not AKnave))) or (BKnave and not ((AKnight and AKnave) or (AKnave and not AKnave)))),

    ((BKnight and CKnave) or (BKnave and not CKnave)),

    ((CKnight and AKnight) or (CKnave and not AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
