document.querySelectorAll('input[type="radio"]').forEach(input => {
    input.addEventListener('change', () => {
        const selectedMention = input.value;
        fetch(`/tri_mention_table/?mention=${selectedMention}`)
            .then(response => response.text())
            .then(data => {
                const tableBody = document.querySelector('#children-table .table__body tbody');
                tableBody.innerHTML = data;
            })
            .catch(error => {
                console.error('Erreur lors de la requête AJAX :', error);
            });
    });
});