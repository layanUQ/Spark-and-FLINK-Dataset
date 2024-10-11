from datasets import load_dataset

# Load the dataset
dataset = load_dataset('stanford-oval/ccnews', split='train')

# Filter Arabic records (assuming the language field contains 'ar' for Arabic)
arabic_dataset = dataset.filter(lambda example: example['language'] == 'ar')

# Optional: Limit to 10 million records
limited_arabic_dataset = arabic_dataset.select(range(min(11_600_000, len(arabic_dataset))))

# Save to disk if needed
limited_arabic_dataset.to_csv('ccnews_arabic_filtered.csv')

print(f"Filtered Arabic records: {len(limited_arabic_dataset)}")