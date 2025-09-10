# Define the acceptable limits for each battery parameter
def get_limits():
  limits = {
    'Temperature': {'lower': 0, 'upper': 45},
    'State of Charge': {'lower': 20, 'upper': 80},
    'Charge Rate': {'upper': 0.8}
    }
  return limits

# Check if a value is within the lower and upper limits for a parameter
def check_range_thresholds(value, lower_limit, upper_limit, vital):
  if value < lower_limit:
    print_breach(vital, 'lower')
    return False
  if value > upper_limit:
    print_breach(vital, 'upper')
    return False
  return True

# Check if a value exceeds only the upper limit for a parameter
def check_high_threshold(value, upper_limit, vital):
  if value > upper_limit:
    print_breach(vital, 'upper')
    return False
  return True

# Print a message indicating which parameter breached which limit
def print_breach(parameter, breach_type):
  print(f'{parameter} breached {breach_type} range!')

# Main function to check if all battery parameters are within their respective limits
def battery_is_ok(temperature, soc, charge_rate):
  limits = get_limits()
  vital_status = [
    check_range_thresholds(temperature, limits['Temperature']['lower'], limits['Temperature']['upper'], 'Temperature'),
    check_range_thresholds(soc, limits['State of Charge']['lower'], limits['State of Charge']['upper'], 'State of Charge'),
    check_high_threshold(charge_rate, limits['Charge Rate']['upper'], 'Charge Rate')
    ]
  if not all(vital_status):
    return False
  return True

# Test cases to validate the battery_is_ok function
if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)        # All vitals within range
  assert(battery_is_ok(50, 85, 0) is False)         # Temperature and SOC above upper limits
  assert(battery_is_ok(0, 20, 0.8) is True)         # All vitals at lower/upper boundaries
  assert(battery_is_ok(-1, 50, 0.5) is False)       # Temperature below lower limit
  assert(battery_is_ok(46, 50, 0.5) is False)       # Temperature above upper limit
  assert(battery_is_ok(25, 19, 0.5) is False)       # SOC below lower limit
  assert(battery_is_ok(25, 81, 0.5) is False)       # SOC above upper limit
  assert(battery_is_ok(25, 70, 0.81) is False)      # Charge Rate above upper limit
