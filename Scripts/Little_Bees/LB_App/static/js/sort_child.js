document.querySelectorAll('input[type="radio"]').forEach(input => {
    input.addEventListener('change', () => {
        const selectedSection = input.value;
        fetch(`/tri_enfants_table/?section=${selectedSection}`)
            .then(response => response.text())
            .then(data => {
                const tableBody = document.querySelector('#children-table .table__body');
                tableBody.innerHTML = data;
            })
            .catch(error => {
                console.error('Erreur lors de la requête AJAX :', error);
            });
    });
});
