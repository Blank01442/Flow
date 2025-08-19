# Concurrency and Parallelism

Flow provides built-in support for concurrency and parallelism through async/await, channels, and lightweight threads.

## Concurrency Keywords

### `async`
Declare an asynchronous function.

```flow
async func fetch_data(url) {
    # Simulate async operation
    print "Fetching data from", url
    return "Data from " + url
}
```

### `await`
Wait for an asynchronous operation to complete.

```flow
let data = await fetch_data("https://api.example.com")
print "Got data:", data
```

### `spawn`
Spawn a new task/thread.

```flow
let task = spawn fetch_data("https://api.example.com")
```

### `channel`
Declare a communication channel.

```flow
channel c
```

### `send`
Send a value to a channel.

```flow
send c, 42
```

### `receive`
Receive a value from a channel.

```flow
receive c, value
print "Received value:", value
```

## Example

```flow
# Channel declaration
channel c

# Async function example
async func fetch_data(url) {
    # Simulate async operation
    print "Fetching data from", url
    return "Data from " + url
}

# Await example
let data = await fetch_data("https://api.example.com")
print "Got data:", data

print "Concurrency features are ready!"
```

Note: Concurrency support is experimental and may have platform-specific behavior.