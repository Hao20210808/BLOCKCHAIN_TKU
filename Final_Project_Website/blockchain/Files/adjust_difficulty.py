def adjust_difficulty(self):
    if len(self.chain) % self.adjust_difficulty_blocks != 1:
        return self.difficulty
    elif len(self.chain) <= self.adjust_difficulty_blocks:
        return self.difficulty
    else:
        start = self.chain[-1*self.adjust_difficulty_blocks-1].timestamp
        finish = self.chain[-1].timestamp
        average_time_consumed = round((finish - start) / (self.adjust_difficulty_blocks), 2)
        if average_time_consumed > self.block_time:
            print(f"Average block time:{average_time_consumed}s. Lower the difficulty")
            self.difficulty -= 1
        else:
            print(f"Average block time:{average_time_consumed}s. High up the difficulty")
            self.difficulty += 1


# Since each block records the current timestamp when the block was mined, 
# we can know the output time of each block (the time it takes to find out the matching nonce).

# If the average block generation time is less than the set block generation time, add 1 to the difficulty, 
# If the average block generation time is greater than the set block generation time, decrease the difficulty by 1.
