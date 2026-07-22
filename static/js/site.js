// WWT Site JavaScript

document.addEventListener('DOMContentLoaded', function() {
  console.log('WWT site loaded');
  
  // Handle cookie consent
  const cookieConsent = document.getElementById('cookieConsent');
  const acceptCookies = document.getElementById('acceptCookies');
  
  if (acceptCookies) {
    acceptCookies.addEventListener('click', function() {
      localStorage.setItem('cookieConsent', 'true');
      if (cookieConsent) {
        cookieConsent.style.display = 'none';
      }
    });
  }
  
  // Show cookie banner if not accepted
  if (!localStorage.getItem('cookieConsent') && cookieConsent) {
    cookieConsent.removeAttribute('hidden');
  }
  
  // Mobile menu toggle
  const navToggler = document.querySelector('.navbar-toggler');
  const navCollapse = document.querySelector('.navbar-collapse');
  
  if (navToggler) {
    navToggler.addEventListener('click', function() {
      if (navCollapse) {
        navCollapse.classList.toggle('show');
      }
    });
  }
});

// Newsletter subscription
function subscribeNewsletter(email) {
  if (!email) {
    alert('Please enter your email');
    return;
  }
  console.log('Subscribing:', email);
}

// WhatsApp button functionality
const whatsappButton = document.querySelector('.whatsapp-button');
if (whatsappButton) {
  whatsappButton.addEventListener('click', function(e) {
    e.preventDefault();
    const phone = '254700000000';
    const message = 'Hello, I am interested in your services.';
    const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
  });
}
