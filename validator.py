import re
from typing import Tuple, Optional


class ContactValidator:
    """Validate phone numbers and email addresses."""
    
    # Email regex pattern
    EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Phone number regex pattern (supports multiple formats)
    PHONE_PATTERN = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, Optional[str]]:
        """
        Validate email address format.
        
        Args:
            email: Email address to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not email or not isinstance(email, str):
            return False, "Email must be a non-empty string"
        
        email = email.strip()
        if re.match(ContactValidator.EMAIL_PATTERN, email):
            return True, None
        return False, "Invalid email format"
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, Optional[str]]:
        """
        Validate phone number format.
        
        Args:
            phone: Phone number to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not phone or not isinstance(phone, str):
            return False, "Phone number must be a non-empty string"
        
        phone = phone.strip()
        # Remove spaces and dashes for processing
        phone_cleaned = re.sub(r'[\s\-\(\)]', '', phone)
        
        if re.match(ContactValidator.PHONE_PATTERN, phone):
            return True, None
        return False, "Invalid phone format"
    
    @staticmethod
    def validate_contact(value: str) -> Tuple[str, bool, Optional[str]]:
        """
        Identify and validate if input is email or phone number.
        
        Args:
            value: Contact value to validate
            
        Returns:
            Tuple of (contact_type, is_valid, error_message)
        """
        if '@' in value:
            is_valid, error = ContactValidator.validate_email(value)
            return 'email', is_valid, error
        else:
            is_valid, error = ContactValidator.validate_phone(value)
            return 'phone', is_valid, error


if __name__ == "__main__":
    # Example usage
    test_cases = [
        "john.doe@example.com",
        "invalid.email",
        "+1(555)123-4567",
        "555-123-4567",
        "invalid-phone",
    ]
    
    validator = ContactValidator()
    for test in test_cases:
        contact_type, is_valid, error = validator.validate_contact(test)
        status = "✓ Valid" if is_valid else f"✗ Invalid: {error}"
        print(f"{test:<30} | Type: {contact_type:<6} | {status}")
