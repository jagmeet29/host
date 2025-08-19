## Model Class & Algorithms—Choosing Your Tools! 🧰

Now that we know how to build models, let's talk about which models to choose and how to actually find the best one. This is where things get really practical!

## Model Class—Your Toolkit of Possibilities 📦

A **model class** $\mathcal{M}$ is basically your toolkit—it's the set of all possible models you could use, typically controlled by a **parameter vector** $\Theta$. Think of it like this: if you're building furniture, your "model class" might be "all possible tables." The **parameters** $\Theta$ would be things like height, width, number of legs, material, etc.

## Example: Linear Functions 📈

For **regression problems**, you might choose the **linear model class**:

$$h(x; \theta, \theta_0) = \theta^T x + \theta_0$$

Here, your **parameter vector** is $\Theta = (\theta, \theta_0)$—these numbers completely define your specific model within the linear class.

Translation: "I'm betting that my output depends on my inputs in a straight-line kind of way, and these parameters tell me exactly what that line looks like!"

## The Big World of Model Classes 🌍

For problems like **classification** and **discrimination**, there are tons of model classes to choose from! We'll spend most of this course exploring them, especially **neural networks** (those are the really exciting ones! 🧠).

Important note: We're focusing on **parametric models**—models with a fixed, finite number of parameters. If you relax this assumption, you get **non-parametric models** (which are cool, but that's a story for another day).

## Model Selection vs. Model Fitting—Two Different Games! 🎯

Here's where people often get confused. There are actually two separate problems:

### Model Selection 🤔

"Which toolkit should I use?" This is about picking a **model class** $\mathcal{M}$ from a set of possible classes. Like deciding: "Should I use linear models, or neural networks, or decision trees?"

### Model Fitting 🔧

"Which specific tool from my chosen toolkit?" Once you've picked your toolkit, this is about finding the best **parameters** $\theta$ within that class. Like saying: "Okay, I chose linear models—now what should the slope and intercept be?"

Pro tip: Sometimes ML practitioners know exactly which model class to use based on experience. Other times, you try several and see which works best!

## Algorithms—The Actual Work! 💪

Once you know what you're looking for (model class) and how to score it (evaluation criteria), you need the **algorithm**—the step-by-step computational instructions to actually find your best model.

## The Optimization Approach 📊

Most of the time, you're trying to find the **parameter vector** $\theta$ that minimizes $E_n(\theta)$ (remember our training error from before?). For many problems, you can use **generic optimization software**—like having a Swiss Army knife that works on lots of different problems.

Example: When fitting a linear model to data, you might use the classic **least-squares minimization algorithm**—it's been around forever and works great!

## Specialized ML Algorithms 🎯

But often, we use algorithms specifically designed for **machine learning problems** or particular **hypothesis classes**. These are like specialized tools built exactly for the job.

## The Rebels—Algorithms That Don't Optimize! 😎

Here's a fun twist: some algorithms don't obviously try to optimize any particular criterion!

Example: The **perceptron algorithm** for finding **linear classifiers**—it's one of the first algorithms we'll study, and it has this rebellious character. It just... works, even though it doesn't look like traditional optimization!

## The Big Picture 🔍

Think of the whole process like this:

1. **Model Class**: "What kind of models am I considering?" (Linear? Neural networks? Trees?)
2. **Model Selection**: "Which model class should I actually use?"
3. **Model Fitting**: "What are the best parameter values within my chosen class?"
4. **Algorithm**: "How do I actually compute all this stuff?"

## Key Takeaway 💡

The beauty of machine learning is that you have choices at every level! You can pick your model class based on the problem, choose your evaluation criteria based on what matters, and select algorithms based on what's computationally feasible. It's like being a chef—you choose your cooking style (model class), decide what "good food" means (evaluation criteria), and then follow recipes (algorithms) to actually make the meal! 👨🍳

The art is in making good choices at each step, and that's what we'll learn throughout this course!

