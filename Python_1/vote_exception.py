candidates = ["A", "B", "C"]

# Replace these IDs with the registered voters for this election.
registered_voters = {"V101", "V102", "V103", "V104", "V105"}

votes = {}       # voter_id -> candidate
revoked = set()  # voter IDs revoked for duplicate attempts

print("=== SIMPLE VOTING SYSTEM ===")
print("Candidates:", ", ".join(candidates))
print("Type 'END' as voter ID to finish.\n")

while True:
    voter_id = input("Enter voter ID: ").strip().upper()

    if voter_id == "END":
        break

    if voter_id not in registered_voters:
        print("Invalid or unregistered voter ID.\n")
        continue

    if voter_id in revoked:
        print("Access revoked. You cannot vote again.\n")
        continue

    if voter_id in votes:
        # Revoke voter for attempting to vote more than once.
        previous_vote = votes.pop(voter_id)
        revoked.add(voter_id)
        print("Duplicate voting attempt detected!")
        print(f"{voter_id} has been revoked.")
        print(f"The previous vote for Candidate {previous_vote} was removed.\n")
        continue

    choice = input(f"Choose candidate ({'/'.join(candidates)}): ").strip().upper()

    if choice not in candidates:
        print("Invalid candidate. Your vote was not recorded.\n")
        continue

    votes[voter_id] = choice
    print("Vote recorded successfully.\n")

print("\n=== ELECTION RESULTS ===")

vote_count = {candidate: 0 for candidate in candidates}

for candidate in votes.values():
    vote_count[candidate] += 1

for candidate, count in vote_count.items():
    print(f"Candidate {candidate}: {count} vote(s)")

print(f"\nValid votes: {len(votes)}")
print(f"Revoked voters: {len(revoked)}")

if not votes:
    print("No valid votes were recorded.")
else:
    highest_votes = max(vote_count.values())
    winners = [
        candidate
        for candidate, count in vote_count.items()
        if count == highest_votes
    ]

    if len(winners) == 1:
        print(f"Winner: Candidate {winners[0]}")
    else:
        print("Tie between:", ", ".join(winners))
