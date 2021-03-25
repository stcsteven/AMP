# Message passing encoder and decoder implementation
The idea behind these algorithms is that how we send messages through unreliable channel.
![Message Passing General Scenario](https://user-images.githubusercontent.com/25889114/112514071-8556d200-8dc7-11eb-8f55-6f9059ddb300.png)


Messages tends to get lost in context when we tried to send those plainly. In order to send messages through unreliable channel with losing the message as minimum as possible, we would like to design encoders and decoders.

Encoders are algorithms that we use to add redundancy to the message. While decoders are algorithms that we use to infer source message and the noise itself after being received from the unreliable channel

# Credits:
https://www.youtube.com/watch?v=BCiZc0n6COY&t=15s