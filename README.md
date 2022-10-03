# What is py-tire-height-calc?

***py-tire-size-calculator*** is a demonstration of calculating the height of a tire given its width, sidewall ratio, and rim size.

Given a tire size of **225/40R16**, we can calculate the tire's height in inches as illustrated in the flowchart below:

```mermaid
flowchart LR;
    id1(225/40R16)-->|tire width|id2(225mm)-->|mm to in|id3(225mm / 25.4 = 8.85 in);
    id1-->|tire aspect ratio|id4(40)-->|divided by 100|id5(.40);
    id1-->|rim size|id7(16 inches);
    id3-->id96(8.85 x .40 = 3.54 in);
    id5-->id96;
    id96-->|x2|id97(7.08 in);
    id97-->|sidewall height|id98(7.08in + 16in);
    id7-->id98;
    id98-->id99(23.08 inches);
```
