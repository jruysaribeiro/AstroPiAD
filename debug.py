import math

# --- INSTRUCTIONS ---
# 1. Copy your 'haversine' function and paste it below.
# 2. Run this script.
# 3. It will tell you if your math is correct or broken.

# [PASTE YOUR FUNCTION HERE]
# It should look something like: def haversine(lat1, lon1, lat2, lon2): ...
def haversine_STUDENT_VERSION(lat1, lon1, lat2, lon2):
    # REPLACE this with your formula
    R = 6371 + 408 # Radius + Altitude
    # ... their math ...
    return 0 

# --- THE TEST BENCH ---
def run_test():
    print("--- DIAGNOSTIC MODE: Haversine Formula ---")
    
    # Known Distance: Porto to Lisbon (approx)
    # Coordinates in Decimal Degrees
    lat_porto = 41.1579
    lon_porto = -8.6291
    lat_lisboa = 38.7223
    lon_lisboa = -9.1393
    
    # Expected result on SURFACE (R=6371) is approx 274 km
    # If we add ISS altitude (R=6779), expected is approx 291 km
    
    try:
        # We try to run their function
        result = haversine_STUDENT_VERSION(lat_porto, lon_porto, lat_lisboa, lon_lisboa)
        
        print(f"Input: Porto -> Lisbon")
        print(f"Your Calculated Distance: {result:.2f} km")
        
        # Check against expected range (270-300km)
        if 270 < result < 300:
            print("✅ STATUS: PASS. Your formula is correct!")
            print(">> If your ISS speed is still wrong, check your TIME calculation.")
        elif result > 10000:
            print("❌ STATUS: FAIL. Result is huge.")
            print(">> HINT: Did you forget to convert degrees to radians?")
            print(">> Fix: lat_rad = math.radians(lat)")
        else:
            print("❌ STATUS: FAIL. Result incorrect.")
            print(">> HINT: Check your Radius (R) units.")
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")

if __name__ == "__main__":
    run_test()