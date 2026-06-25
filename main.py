import json
import os

CONFIG_FILE = "config.json"

def load_config():
    """Loads business rules from the configuration file."""
    if not os.path.exists(CONFIG_FILE):
        print(f"Info: Configuration file '{CONFIG_FILE}' not found. Creating a default one.")
        # Create a default config for first run, demonstrating initial business rules
        default_config = {
            "discount_rules": {
                "base_percentage": 5, # Default discount for all customers
                "premium_threshold": 200, # Order value threshold for premium discount
                "premium_percentage": 10 # Discount for premium customers above threshold
            },
            "shipping_rules": {
                "base_cost": 10, # Standard shipping cost
                "free_shipping_threshold": 150 # Order value threshold for free shipping
            }
        }
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(default_config, f, indent=2)
            print(f"Default '{CONFIG_FILE}' created. Please run the script again to process orders with these rules.")
        except Exception as e:
            print(f"Error creating default config file: {e}")
        return None

    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        return config
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{CONFIG_FILE}'. Please check its format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading config: {e}")
        return None

def process_order(order_id, order_value, is_premium_customer):
    """
    Processes an order by applying business rules loaded from configuration.
    This demonstrates how software can adapt quickly to changing business needs
    by externalizing rules.
    """
    config = load_config()
    if config is None:
        return # Exit if config loading failed or default was just created

    print(f"\n--- Processing Order {order_id} (Value: ${order_value:.2f}, Premium: {is_premium_customer}) ---")

    # --- Apply Discount Rules (configured externally) ---
    # The software's discount logic is driven by external parameters.
    # Business can change these percentages/thresholds without code changes.
    discount_rules = config.get("discount_rules", {})
    base_percentage = discount_rules.get("base_percentage", 0)
    premium_threshold = discount_rules.get("premium_threshold", 0)
    premium_percentage = discount_rules.get("premium_percentage", 0)

    discount_amount = 0
    if is_premium_customer and order_value >= premium_threshold:
        discount_amount = order_value * (premium_percentage / 100)
        print(f"  Applied Premium Discount ({premium_percentage}%): -${discount_amount:.2f}")
    else:
        discount_amount = order_value * (base_percentage / 100)
        print(f"  Applied Base Discount ({base_percentage}%): -${discount_amount:.2f}")

    value_after_discount = order_value - discount_amount

    # --- Apply Shipping Rules (configured externally) ---
    # Shipping costs and free shipping conditions are also externalized.
    # This allows rapid adjustments to logistics policies.
    shipping_rules = config.get("shipping_rules", {})
    base_shipping_cost = shipping_rules.get("base_cost", 0)
    free_shipping_threshold = shipping_rules.get("free_shipping_threshold", 0)

    shipping_cost = base_shipping_cost
    if value_after_discount >= free_shipping_threshold:
        shipping_cost = 0
        print(f"  Free Shipping Applied (Order value >= ${free_shipping_threshold:.2f})")
    else:
        print(f"  Shipping Cost: +${shipping_cost:.2f}")

    final_total = value_after_discount + shipping_cost

    print(f"  Value after discount: ${value_after_discount:.2f}")
    print(f"  Final Total: ${final_total:.2f}")
    print("--------------------------------------------------")


if __name__ == "__main__":
    print("--- Initial Run with Current Business Rules ---")
    # Simulate an initial set of orders
    process_order(1, 120.00, False)
    process_order(2, 250.00, True)
    process_order(3, 180.00, False)

    print("\n--- To demonstrate rapid adaptation: ---")
    print(f"1. Edit the '{CONFIG_FILE}' file (e.g., change 'base_percentage' from 5 to 10, or 'free_shipping_threshold' from 150 to 100).")
    print("2. Save the file.")
    print("3. Run 'python main.py' again to see the immediate effect of the new business rules without changing any code.")
    print("   This illustrates how the software adapts instantly to new business requirements, providing a competitive advantage.")
