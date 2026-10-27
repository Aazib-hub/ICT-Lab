storage gb = float(input("Enter storage in GB: "))
storage mb = storage gb * 1024
total = estimate_storage(num_files, avg_size)
print(total)
