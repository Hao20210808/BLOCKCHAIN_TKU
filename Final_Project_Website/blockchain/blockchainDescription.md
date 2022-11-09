# The composition of the transaction
First, define the format and content of some basic transactions and blocks.


## Transaction
- Each transaction will generate a transaction detail, record the:
  - sender,
  - receiver,
  - amount,
  - handling fee
  - remarks of the transaction in detail. 


- The details of each transaction here are called **Transaction**.


## Blocks of transactions
- All **Transactions** will be placed into blocks in chronological order. 

- When a new block is being produced, all newly generated transaction records will be placed under the block.

## Transaction format
A transaction has this information

- sender
  - the initiator of the transaction, and at the same time confirm whether the balance of the sender is sufficient

- receiver
  - The recipient of the transaction, usually the amount of the payment can be received without the user's consent

- amounts
  - the amount of the transaction

- fee
  - the amount of handling fee to be paid during the transaction

- message/content
  - leave information like a remark on a transfer, usually for the recipient to see

## Block format
- Each block contains many transactions

- For encryption requirements, the **hash value** of the previous block will be recorded.
  - **hash value** can be thought of as the lock on each block

---
The **nonce** mined by the miner represents the key (or another lock) that can match the lock, and the **hash value** of the next block is generated according to this **nonce value**. 
So that as long as any one of the transaction records, block If the block is tampered with, the **nonce** and **hash** on the entire chain need to be fixed

## Blockchain Architecture


## Hash

## genesis block
- The first block produced when starting to deploy the blockchain

- It does not need to carry any transaction records, it is an empty block without any data

## Put the transaction record in the new block


## Mining new blocks

## Adjust mining difficulty

## Calculate account balance

## Check if the hash value is correct
