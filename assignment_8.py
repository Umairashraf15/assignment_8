class Bucket:
    def __init__(self, capacity: int) -> None:
        """Initialize a bucket with a given capacity."""
        self.capacity: int = capacity  # Maximum capacity of the bucket
        self.current: int = 0  # Current amount of water in the bucket

    def fill(self) -> None:
        """Fill the bucket to its full capacity."""
        self.current = self.capacity

    def empty(self) -> None:
        """Empty the bucket."""
        self.current = 0

    def pour_into(self, other: 'Bucket') -> None:
        """
        Pour water from this bucket into another bucket (other).
        The amount poured will be limited by the remaining capacity of the other bucket.
        """
        amount_to_pour: int = min(self.current, other.capacity - other.current)
        self.current -= amount_to_pour
        other.current += amount_to_pour

    def __str__(self) -> str:
        """Return a string representation of the bucket's current state."""
        return f"{self.current}/{self.capacity}L"


def print_buckets(bucket8: Bucket, bucket5: Bucket, bucket3: Bucket) -> None:
    """Print the visual representation of the buckets' current water levels."""
    print(f"""
    Try to get 4L of water into one of these buckets:

    8|{'W' * bucket8.current}{' ' * (8 - bucket8.current)}|
    7|{'W' * bucket8.current}{' ' * (7 - bucket8.current)}|
    6|{'W' * bucket8.current}{' ' * (6 - bucket8.current)}|
    5|{'W' * bucket8.current}{' ' * (5 - bucket8.current)}|        5|{'W' * bucket5.current}{' ' * (5 - bucket5.current)}|
    4|{'W' * bucket8.current}{' ' * (4 - bucket8.current)}|        4|{'W' * bucket5.current}{' ' * (4 - bucket5.current)}|
    3|{'W' * bucket8.current}{' ' * (3 - bucket8.current)}|        3|{'W' * bucket5.current}{' ' * (3 - bucket5.current)}|        3|{'W' * bucket3.current}{' ' * (3 - bucket3.current)}|
    2|{'W' * bucket8.current}{' ' * (2 - bucket8.current)}|        2|{'W' * bucket5.current}{' ' * (2 - bucket5.current)}|        2|{'W' * bucket3.current}{' ' * (2 - bucket3.current)}|
    1|{'W' * bucket8.current}{' ' * (1 - bucket8.current)}|        1|{'W' * bucket5.current}{' ' * (1 - bucket5.current)}|        1|{'W' * bucket3.current}{' ' * (1 - bucket3.current)}|
     +------+         +------+         +------+
        8L               5L               3L
    """)


def select_bucket(buckets: dict[str, Bucket], prompt: str) -> Bucket:
    """Prompt the user to select a bucket (8, 5, or 3) and return the corresponding bucket object."""
    while True:
        choice: str = input(prompt).strip()
        if choice in ['8', '5', '3']:
            return buckets[choice]
        elif choice.lower() == 'quit':
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 8, 5, or 3.")


def check_solution(bucket8: Bucket, bucket5: Bucket, bucket3: Bucket) -> bool:
    """Check if any of the buckets has exactly 4 liters of water."""
    return bucket8.current == 4 or bucket5.current == 4 or bucket3.current == 4


def solve_bucket_puzzle() -> None:
    """Run the interactive bucket puzzle solver."""
    # Create bucket objects with their respective capacities
    bucket8: Bucket = Bucket(8)
    bucket5: Bucket = Bucket(5)
    bucket3: Bucket = Bucket(3)
    
    # Map bucket numbers to their respective objects
    buckets: dict[str, Bucket] = {'8': bucket8, '5': bucket5, '3': bucket3}
    
    # Main game loop
    while True:
        # Print the current state of the buckets
        print_buckets(bucket8, bucket5, bucket3)
        
        # Check if any bucket has exactly 4 liters of water
        if check_solution(bucket8, bucket5, bucket3):
            print("Congratulations! You got exactly 4 liters of water!")
            break
        
        # Get user action
        action: str = input("(F)ill the bucket, (E)mpty the bucket, (P)our one bucket into another, or (Q)uit: ").strip().lower()
        
        if action == 'f':
            # Fill a selected bucket
            fill_bucket: Bucket = select_bucket(buckets, "Select a bucket (8, 5, 3, or QUIT): ")
            fill_bucket.fill()
        
        elif action == 'e':
            # Empty a selected bucket
            empty_bucket: Bucket = select_bucket(buckets, "Select a bucket to empty (8, 5, 3, or QUIT): ")
            empty_bucket.empty()
        
        elif action == 'p':
            # Pour water from one bucket into another
            from_bucket: Bucket = select_bucket(buckets, "Select the bucket to pour from (8, 5, 3, or QUIT): ")
            to_bucket: Bucket = select_bucket(buckets, "Select the bucket to pour into (8, 5, 3, or QUIT): ")
            from_bucket.pour_into(to_bucket)
        
        elif action == 'q':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter F, E, P, or Q.")

# Run the interactive puzzle solver
solve_bucket_puzzle()
