// var petText = document.getElementsByClassName("petition__text")[0];
// var petForm = document.getElementsByClassName("petition__form")[0];
// var petSwitch = document.getElementsByClassName("petition__switch")[0];
// // petSwitch.innerHTML = "Zeige Forderungen"
// 
// var petFocus = 'textt';
// 
// if (petText.clientHeight < 400) {
//   petSwitch.style.display = 'block';
// }
// 
// function changePetitionFocus() {
//   if(!petText.classList.contains('grow')) {
//     petFocus = 'text';
//     petForm.classList.remove("grow");
//     petText.classList.remove("shrink");
//     petText.classList.add("grow");
//     petForm.classList.add("shrink");
//     // petSwitch.innerHTML = "Zeige Formular"
//     petSwitch.classList.add("go-up");
//     petSwitch.classList.remove("go-down");
//   } else {
//     focusOnForm()
//   }
// }
// 
// function focusOnForm() {
//   petFocus = 'form';
//   petText.classList.remove("grow");
//   petForm.classList.add("grow");
//   petForm.classList.remove("shrink");
//   petText.classList.add("shrink");
//   // petSwitch.innerHTML = "Zeige Forderungen"
//   petSwitch.classList.add("go-down");
//   petSwitch.classList.remove("go-up");
// }
// 
// petSwitch.onclick = changePetitionFocus;
// 
// petForm.onclick = focusOnForm;
