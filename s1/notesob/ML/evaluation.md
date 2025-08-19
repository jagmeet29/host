# How Do We Know If We're Doing Well?

Once you've figured out what type of ML problem you're tackling, the next big question is: *How do we measure success?* This is where **evaluation criteria** come in—basically, your report card for how well your ML system is performing!

## Loss Functions: The "Ouch" Meter

A **loss function** $L(g,a)$ is like your personal disappointment meter. It tells you exactly how much it hurts when you guess $g$ but the real answer was $a$. Think of it as "how sad are we when we chose $g$ instead of $a$". Here are the most popular ways to measure that sadness:

### 0-1 Loss (The Simple "Right or Wrong")

$L(g,a) = \begin{cases} 0 & \text{if } g = a \\ 1 & \text{otherwise} \end{cases}$

Perfect for **classification**—you either nailed it (no penalty) or you didn't (full penalty). It's that black-and-white!

### Squared Loss (The "How Far Off" Measure)

$L(g,a) = (g-a)^2$

Great for **regression**. If you predicted house prices at $300,000 but it was actually $350,000, you get penalized by $(300,000 - 350,000)^2$. The further off you are, the more it hurts!

### Linear Loss (The "Absolute Distance")

$L(g,a) = |g-a|$

Like squared loss, but less dramatic—it doesn't punish big mistakes as harshly.

### Asymmetric Loss (When Some Mistakes Are Worse)

$L(g,a) = \begin{cases} 1 & \text{if } g=1 \text{ and } a=0 \\ 100 & \text{if } g=0 \text{ and } a=1 \\ 0 & \text{otherwise} \end{cases}$

Perfect example: heart attack detection. Missing a real heart attack (predicting "no" when it's "yes") is 100x worse than a false alarm!

## The Big Picture: Overall System Performance

Individual predictions are nice, but we need to judge the whole system. Here are the main approaches:

- **Minimizing Expected Loss** (also called **risk**): What's our average performance going to be?
- **Minimizing Maximum Loss**: What's the worst-case scenario?
- **Minimizing Regret**: How much worse are we than the absolute best possible approach?
- **Asymptotic Behavior**: How will we do with infinite training data?
- **Probably Approximately Correct**: Are we usually right, most of the time?

The gold standard? **Expected loss minimization**—it's like optimizing for long-term success rather than worrying about individual bad days.

## Model Types: How Do We Actually Make Predictions?

### No Model (The Direct Approach)

Sometimes you can skip the middleman! With methods like **nearest neighbor**, you just look at your training data directly and say, "Hey, what happened in similar situations before?"

### Prediction Rule (The Two-Step Dance)

This is the classic approach:

1. **Fit** a model to your training data
2. **Use** that model to make new predictions

You create a **prediction rule** $y = h(x; \theta)$, where:
- $h$ is your chosen function type
- $\theta$ are the **parameters** you learn from data
- For new input $x^{(n+1)}$, you predict $h(x^{(n+1)}; \theta)$

## The Fitting Process: Finding the Best Parameters

Here's where the magic happens! We want to find the $\theta$ that makes our model awesome. The **training error** approach says:

$E_n(\theta) = \frac{1}{n}\sum_{i=1}^n L(h(x^{(i)}; \theta), y^{(i)})$

This means: "Find the $\theta$ that minimizes our average loss on the training data."

### But Wait—There's a Catch!

Just minimizing **training error** can be dangerous. It's like studying only the practice test and then bombing the real exam. You might get so good at your training data that you completely fail on new, unseen data. This is the classic **overfitting** problem!

The real goal? Minimize **test error**—how well you perform on completely new data. But since we don't have that data yet, we need to be smart about how we train our models.

## Key Takeaway

**Evaluation criteria** are your compass in the ML world. They tell you not just whether you're moving, but whether you're moving in the right direction. Pick the wrong loss function or evaluation method, and you might optimize for the wrong thing entirely—like training a heart attack detector that never wants to "bother" anyone with false alarms! Choose wisely, and your ML system will thank you (and so will the people using it)!

