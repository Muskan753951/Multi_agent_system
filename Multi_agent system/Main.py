from coordinator import run_pipeline

if __name__ == "__main__":
    user_goal = input("Enter your goal: ")
    result = run_pipeline(user_goal)

    print("\n=== Final Result ===")
    if "summary" in result:
        print(result["summary"])
    else:
        print(result)
