function _3dsec(STRIPE_PUBLIC_KEY, payment_intent_secret) {
    document.addEventListener("DOMContentLoaded", function(event){
      var stripe = Stripe(STRIPE_PUBLIC_KEY);

      stripe.confirmCardPayment(payment_intent_secret).then(function(result) {
        if (result.error) {
          // Display error
          $("#3d_secure_output").text("Error!");
          $("#3d_secure_output").addClass("red-text accent-4");
        } else {
          // Display a success
          $("#3d_secure_output").text("Thank you for payment");
          $("#3d_secure_output").addClass("indigo-text accent-2");
        }
      });
    });
}
