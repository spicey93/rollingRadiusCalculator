# Rolling Radius Calculator
A Python GUI application where you can enter any tyre size and find alternative sizes with a similar rolling radius.

## What Problem Does It Solve?
As a tyre technician, I often get asked by customers what size tyres they could fit to their vehicle without it significantly affecting the performance and handling characteristics. In order to answer this question, I would need to work out the rolling radius of their vehicles current tyre size and then compare that value to a range of other tyre sizes. This can be a time-consuming process.

## How Does It Work?
The user simply enters the tyre width, profile, and diameter that the customer currently has fitted to their vehicle. The programme will then calculate the rolling radius of the tyre and then query a database for matching values. A value is considered a match if it is within -+0.5% of the original rolling radius.

