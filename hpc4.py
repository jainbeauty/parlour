import multiprocessing

def process_data(data_chunk):
    """
    Function to process a chunk of data.
    """
    # Your data processing logic goes here
    processed_data = [d * 2 for d in data_chunk]
    return processed_data

if __name__ == '__main__':
    # Create some sample data
    data = list(range(100000))

    # Split the data into chunks
    chunk_size = 1000
    data_chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    # Create a pool of worker processes
    num_processes = multiprocessing.cpu_count()
    print('Number of processes: ', num_processes)
    pool = multiprocessing.Pool(num_processes)

    # Process the data in parallel
    processed_chunks = pool.map(process_data, data_chunks)

    # Concatenate the processed chunks into a single list
    processed_data = []
    for chunk in processed_chunks:
        processed_data.extend(chunk)

    print(processed_data[:100])
