def remove_duplicate_emails(input_file, output_file):
    seen = set()

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            email = line.strip()
            # If email is new, save it
            if email and email not in seen:
                seen.add(email)
                outfile.write(email + "\n")

    print(f"yes Duplicate removal complete!\nOutput saved to: {output_file}")
    print(f"Total unique emails: {len(seen)}")


if __name__ == "__main__":
    input_file = "emails.txt"
    output_file = "unique_emails.txt"

    remove_duplicate_emails(input_file, output_file)
