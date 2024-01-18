function addMemo() {
    const memoInput = document.getElementById('memoInput');
    const memoText = memoInput.value.trim();

    if (memoText !== '') {
        fetch('/add_memo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: memoText }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                memoInput.value = '';
                fetchMemos();
            } else {
                alert('Failed to add memo');
            }
        });
    }
}

function fetchMemos() {
    fetch('/get_memos')
        .then(response => response.json())
        .then(data => {
            const memoList = document.getElementById('memoList');
            memoList.innerHTML = '';

            data.memos.forEach(memo => {
                const listItem = document.createElement('li');
                listItem.textContent = memo;
                memoList.appendChild(listItem);
            });
        });
}

// Fetch memos on page load
document.addEventListener('DOMContentLoaded', fetchMemos);