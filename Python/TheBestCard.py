import sys


def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True


def main():
  # Đọc toàn bộ input từ file input.txt truyền vào
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  t = int(input_data[0])
  results = []

  for i in range(1, t + 1):
    n = int(input_data[i])
    # Kiểm tra tính nguyên tố của n + 1
    if is_prime(n + 1):
      results.append("YES")
    else:
      results.append("NO")

  # In toàn bộ kết quả ra màn hình
  print("\n".join(results))


if __name__ == "__main__":
  main()