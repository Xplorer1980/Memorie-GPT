// ==UserScript==
// @name         Auto Save Partial File ChatGPT + Button Control (Super Edition)
// @namespace    http://tampermonkey.net/
// @version      2.0
// @description  AutoSave file ChatGPT ogni X minuti configurabili, timer visivo, suono, salvataggio forzato, filtro per titolo con S, retry automatico
// @match        *://chatgpt.com/*
// @match        *://www.chatgpt.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    let active = false;
    let intervalId;
    let countdownInterval;
    let intervalTime = 15 * 60 * 1000; // Default 15 minuti
    const retryTime = 30 * 1000; // 30 secondi
    let timeLeft = intervalTime;

    const messageText = "Genera immediatamente un file fisico scaricabile (txt, md o zip) con il parziale aggiornato dell'elaborazione in corso. Non incollare il contenuto in Canvas. Non inserire codice. Crea solo un file scaricabile pronto per il download. Nomina il file con il nome della chat attuale seguito da un numero incrementale progressivo. Nessuna conferma richiesta.";

    function sendMessage() {
        if (!document.title.trim().startsWith('S')) {
            console.log('Titolo non valido, script inattivo.');
            return;
        }
        const textarea = document.querySelector('textarea');
        if (textarea) {
            textarea.value = messageText;
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
            const buttons = document.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.innerText.toLowerCase().includes('send') || btn.innerText.toLowerCase().includes('invio')) {
                    btn.click();
                }
            });
        }
    }

    function checkAndDownload() {
        const links = document.querySelectorAll('a');
        let foundDownload = false;

        links.forEach(link => {
            const href = link.getAttribute('href');
            if (href && (href.endsWith('.txt') || href.endsWith('.md') || href.endsWith('.zip'))) {
                link.click();
                foundDownload = true;
                playBeep();
            }
        });

        if (!foundDownload) {
            console.log("Nessun file trovato, ritentativo in corso...");
            setTimeout(() => {
                if (active) {
                    sendMessage();
                    setTimeout(checkAndDownload, retryTime);
                }
            }, 1000);
        }
    }

    function playBeep() {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioCtx.createOscillator();
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(1000, audioCtx.currentTime);
        oscillator.connect(audioCtx.destination);
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.2);
    }

    function startAutoSave() {
        if (!active) return;

        sendMessage();
        setTimeout(checkAndDownload, retryTime);

        intervalId = setInterval(() => {
            timeLeft = intervalTime;
            sendMessage();
            setTimeout(checkAndDownload, retryTime);
        }, intervalTime);

        countdownInterval = setInterval(updateTimer, 1000);
    }

    function stopAutoSave() {
        active = false;
        clearInterval(intervalId);
        clearInterval(countdownInterval);
        if (document.getElementById('countdownTimer')) {
            document.getElementById('countdownTimer').textContent = '';
        }
        console.log('AutoSave script fermato.');
    }

    function updateTimer() {
        if (timeLeft <= 0) return;
        timeLeft -= 1000;
        if (document.getElementById('countdownTimer')) {
            const minutes = Math.floor((timeLeft / 1000) / 60);
            const seconds = Math.floor((timeLeft / 1000) % 60);
            document.getElementById('countdownTimer').textContent = `Prossimo salvataggio: ${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        }
    }

    function createControlElements() {
        if (document.getElementById('autoSaveButton')) return;

        const container = document.createElement('div');
        container.style.position = 'fixed';
        container.style.bottom = '10px';
        container.style.right = '10px';
        container.style.zIndex = 9999;
        container.style.display = 'flex';
        container.style.flexDirection = 'column';
        container.style.alignItems = 'flex-end';
        container.style.gap = '5px';

        const input = document.createElement('input');
        input.type = 'number';
        input.min = '1';
        input.placeholder = 'Minuti';
        input.style.padding = '5px';
        input.style.border = '1px solid #ccc';
        input.style.borderRadius = '5px';

        const controlButton = document.createElement('button');
        controlButton.id = 'autoSaveButton';
        controlButton.innerHTML = '▶️ Start AutoSave';
        controlButton.style.padding = '10px';
        controlButton.style.backgroundColor = '#4CAF50';
        controlButton.style.color = 'white';
        controlButton.style.border = 'none';
        controlButton.style.borderRadius = '5px';
        controlButton.style.cursor = 'pointer';

        const manualSaveButton = document.createElement('button');
        manualSaveButton.innerHTML = '💾 Salva subito';
        manualSaveButton.style.padding = '5px';
        manualSaveButton.style.backgroundColor = '#2196F3';
        manualSaveButton.style.color = 'white';
        manualSaveButton.style.border = 'none';
        manualSaveButton.style.borderRadius = '5px';
        manualSaveButton.style.cursor = 'pointer';

        const countdown = document.createElement('div');
        countdown.id = 'countdownTimer';
        countdown.style.color = '#333';
        countdown.style.fontSize = '12px';
        countdown.style.marginTop = '5px';

        controlButton.addEventListener('click', function() {
            if (!active) {
                if (input.value) {
                    intervalTime = parseInt(input.value) * 60 * 1000;
                    timeLeft = intervalTime;
                }
                active = true;
                controlButton.innerHTML = '⏹ Stop AutoSave';
                controlButton.style.backgroundColor = '#f44336';
                startAutoSave();
            } else {
                stopAutoSave();
                controlButton.innerHTML = '▶️ Start AutoSave';
                controlButton.style.backgroundColor = '#4CAF50';
            }
        });

        manualSaveButton.addEventListener('click', function() {
            sendMessage();
            setTimeout(checkAndDownload, retryTime);
        });

        container.appendChild(input);
        container.appendChild(controlButton);
        container.appendChild(manualSaveButton);
        container.appendChild(countdown);
        document.body.appendChild(container);
    }

    function waitForBodyAndInject() {
        const observer = new MutationObserver(() => {
            if (document.body && !document.getElementById('autoSaveButton')) {
                createControlElements();
            }
        });
        observer.observe(document.documentElement, { childList: true, subtree: true });
    }

    waitForBodyAndInject();
})();
