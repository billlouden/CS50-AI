# Python to solve knights vs knaves based on 4 puzzles (0 - 3)
# Bill Louden

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# (A v B) ^ (A ^ B)
# Knight always tells true Knave could lie.
# cannot be both. ergo False
knowledge0 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    Implication(AKnave,Not(And(AKnight,AKnave))),
    Implication(AKnight,(And(AKnight,AKnave)))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    Implication(AKnave,Not(And(AKnave,BKnave))),
    Implication(AKnight,(And(AKnave,BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    Implication(AKnight,Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    Implication(AKnave, Not(Or(And(AKnave,BKnave),And(AKnight,BKnight)))),
    Implication(BKnight,Or(And(AKnave,BKnight),And(BKnave,AKnight))),
    Implication(BKnave, Not(Or(And(AKnave,BKnight),And(BKnave,AKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))),
    Implication(BKnave,Not(CKnave)),
    Implication(BKnight,CKnave),
    Implication(CKnave,Not(AKnight)),
    Implication(CKnight,AKnight),
    Implication(AKnave,Not(Or(AKnight,AKnave))),
    Implication(AKnight,Or(AKnight,AKnave))

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
