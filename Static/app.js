const form = document.querySelector('.login-form');
const message = document.querySelector('.message');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const username = form.querySelector('input[type="text"]').value;
  const password = form.querySelector('input[type="password"]').value;
  // Patikriname, ar vartotojo vardas ir slaptažodis yra teisingi
  if (username === 'admin' && password === 'password') {
    // Nukreipiame vartotoją į pagrindinį puslapį
    window.location.href = '/home';
  } else {
    // Jei duomenys yra neteisingi, pranešame vartotojui klaidos pranešimą
    message.textContent = 'Invalid username or password';
    message.style.color = 'red';
  }
});
