import google.generativeai as genai
genai.configure(api_key="AIzaSyD9Gi3C3IWovq8BvLykbheaWU8XmUqKBDs")

def get_recommendations(predicted_co2):
    """
    Generates CO2 emission reduction recommendations based on the predicted value.

    :param predicted_co2: The predicted CO2 emission value.
    :return: AI-generated recommendation.
    """
    car_recommendation1 = "Example Car 1"  # Define the variable with an example value
    car_recommendation2 = "Example Car 2"  # Define the variable with an example value
    car_recommendation3 = "Example Car 3"  # Define the variable with an example value

    car1_emissions = "Example Emissions 1" # Define the variable with an example value
    car2_emissions = "Example Emissions 2" # Define the variable with an example value
    car3_emissions = "Example Emissions 3" # Define the variable with an example value

    car1_savings = "Example Savings 1"  # Define the variable with an example value
    car2_savings = "Example Savings 2"  # Define the variable with an example value
    car3_savings = "Example Savings 3"  # Define the variable with an example value

    car1_price = "Example Price 1"  # Define the variable with an example value    
    car2_price = "Example Price 2"  # Define the variable with an example value
    car3_price = "Example Price 3"  # Define the variable with an example value


    recommendation_car = "Example Car"  # Define the variable with an example value
    annual_savings = "Example Savings"  # Define the variable with an example value
    easy_recommendation = "Example Recommendation"  # Define the variable with an example value
    longterm_recommendation = "Example Recommendation"  # Define the variable with an example value
    roi_period = "Example Period"  # Define the variable with an example value

    prompt = f"""
The predicted CO2 emission for this vehicle is {predicted_co2} g/km.
Provide ONLY the HTML report with the values filled in. Do not include any explanations or key considerations. Don't include disclamer, extra comments and html tag in the final result.

<div style="background-color: #121212; color: #e0e0e0; padding: 20px; font-family: Arial, sans-serif;">
<h2 style="color: #4caf50;">🚗 CO2 Emission Analysis</h2>
<p>Your vehicle emits <b>{predicted_co2} g/km</b> of CO2.</p>

<h3 style="text-align: center; color: #64b5f6;">🌍 Real-World Comparison</h3>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; border-color: #424242;">
  <tr style="background-color: #1e1e1e;"><th style="color: #64b5f6;">Comparison</th><th style="color: #64b5f6;">Value</th></tr>
  <tr><td>Average Indian Sedan</td><td>XX g/km</td></tr>
  <tr><td>Fuel-Efficient Car (Toyota Prius, Tata Nexon EV)</td><td>XX g/km</td></tr>
  <tr><td>Annual Emission (15,000 km/year)</td><td>XX tons of CO2</td></tr>
  <tr><td>Equivalent Trees Needed</td><td>XX trees</td></tr>
</table>

<h3 style="text-align: center; color: #81c784;">💰 Cost of Carbon Offset (₹ INR)</h3>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; border-color: #424242;">
  <tr style="background-color: #1e1e1e;"><th style="color: #81c784;">Method</th><th style="color: #81c784;">Cost (₹)</th></tr>
  <tr><td>Carbon Credits</td><td>XX per year</td></tr>
  <tr><td>Tree Planting</td><td>XX per year</td></tr>
  <tr><td>Renewable Energy Investment</td><td>XX per year</td></tr>
</table>

<h3 style="text-align: center; color: #ffb74d;">⛽ Fuel Cost Estimation (₹ INR)</h3>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; border-color: #424242;">
  <tr style="background-color: #1a1a1a;"><th style="color: #ffb74d;">Vehicle Type</th><th style="color: #ffb74d;">Annual Fuel Cost (₹)</th><th style="color: #ffb74d;">Annual Savings (₹)</th></tr>
  <tr><td>Current Vehicle</td><td>₹XX</td><td>-</td></tr>
  <tr><td>Hybrid (Maruti Grand Vitara Hybrid)</td><td>₹XX</td><td>₹XX</td></tr>
  <tr><td>EV (Tata Nexon EV)</td><td>₹XX</td><td>₹XX</td></tr>
</table>

<h3 style="text-align: center; color: #f48fb1;">🚦 Top 3 Driving Tips for Your Vehicle</h3>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; border-color: #424242;">
  <tr style="background-color: #1e1e1e;"><th style="color: #f48fb1;">Tip</th><th style="color: #f48fb1;">Potential CO2 Reduction</th><th style="color: #f48fb1;">Annual Savings (₹)</th></tr>
  <tr><td>Maintain Steady Speed (60-80 km/h)</td><td>XX%</td><td>₹XX</td></tr>
  <tr><td>Keep Tires Properly Inflated</td><td>XX%</td><td>₹XX</td></tr>
  <tr><td>Turn Off Engine When Idle > 30 seconds</td><td>XX%</td><td>₹XX</td></tr>
</table>

<h3 style="text-align: center; color: #90caf9;">🔄 Recommended Alternatives Based on Your Emissions</h3>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; border-color: #424242;">
  <tr style="background-color: #1e1e1e;"><th style="color: #90caf9;">Vehicle</th><th style="color: #90caf9;">CO2 Emission (g/km)</th><th style="color: #90caf9;">Annual Savings (₹)</th><th style="color: #90caf9;">Price Range (₹)</th></tr>
  <tr><td>{car_recommendation1}</td><td>{car1_emissions}</td><td>₹{car1_savings}</td><td>₹{car1_price}</td></tr>
  <tr><td>{car_recommendation2}</td><td>{car2_emissions}</td><td>₹{car2_savings}</td><td>₹{car2_price}</td></tr>
  <tr><td>{car_recommendation3}</td><td>{car3_emissions}</td><td>₹{car3_savings}</td><td>₹{car3_price}</td></tr>
</table>

<div style="background-color: #263238; padding: 15px; margin-top: 20px; border-radius: 5px;">
  <h3 style="color: #4fc3f7;">⚡ Quick Action Steps</h3>
  <p>Based on your emissions of {predicted_co2} g/km, here are your 3 most impactful actions:</p>
  <ol style="color: #e0e0e0;">
    <li><b style="color: #80deea;">Most Impactful Action:</b> {recommendation_car} - Potential annual savings: ₹{annual_savings}</li>
    <li><b style="color: #80deea;">Easy Implementation:</b> {easy_recommendation} - Can be done immediately</li>
    <li><b style="color: #80deea;">Long-term Solution:</b> {longterm_recommendation} - ROI in {roi_period}</li>
  </ol>
</div>
</div>

Important instructions:
1. Use current, accurate data for Indian market conditions (March 2025)
2. Calculate all comparison percentages, costs and savings precisely
3. Use realistic fuel prices in India for all calculations
4. Replace all XX placeholders with actual calculated values
5. Present information in a factual, actionable manner
6. Format tables cleanly with proper alignment and spacing
7. Ensure all monetary values show the ₹ symbol consistently
8. Tailor recommendations specifically to the {predicted_co2} g/km emission level
9. Replace all car_recommendation1, car1_emissions, car1_savings, car1_price, car_recommendation2, car2_emissions, car2_savings, car2_price, car_recommendation3, car3_emissions, car3_savings, car3_price, placeholders with specific cars and values under the given emission level
10.Replace all recommendation_car, easy_recommendation, annual_savings, longterm_recommendations, roi_period placeholders with actual calculated values and recommendations.
11. do not show key considerations, assumptions, or calculations in the final report and provide a one line disclaimer at the end of the report only.
12. DO NOT add any text after the HTML content
13. DO NOT include any disclaimers except one single line at the very end
14. ONLY return the HTML content with the values filled in
"""

    response = genai.GenerativeModel("gemini-1.5-pro").generate_content(prompt)
    return response.text