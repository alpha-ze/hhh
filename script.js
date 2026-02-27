const API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:8000' 
    : 'https://' + window.location.hostname + '/api';

const AGENT_BASE_URL = window.location.hostname === 'localhost'
    ? 'http://localhost:8001'
    : 'https://' + window.location.hostname + '/agent';

document.getElementById('eligibilityForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const userProfile = {};
    
    for (let [key, value] of formData.entries()) {
        if (value !== '') {
            if (key === 'age' || key === 'income' || key === 'child_age') {
                userProfile[key] = parseFloat(value);
            } else {
                userProfile[key] = value;
            }
        }
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/check-eligibility`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userProfile)
        });
        
        if (!response.ok) {
            throw new Error('Failed to check eligibility');
        }
        
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        alert('Error: ' + error.message + '\n\nMake sure the backend server is running on port 8000');
    }
});

function displayResults(data) {
    const resultsSection = document.getElementById('results');
    const schemesList = document.getElementById('schemesList');
    
    resultsSection.style.display = 'block';
    
    if (data.total_eligible === 0) {
        schemesList.innerHTML = `
            <div class="no-schemes">
                <h3>No eligible schemes found</h3>
                <p>Based on your profile, you don't currently qualify for any schemes. Try updating your information.</p>
            </div>
        `;
        return;
    }
    
    schemesList.innerHTML = `
        <p style="color: #28a745; font-weight: 600; margin-bottom: 20px;">
            ✓ You are eligible for ${data.total_eligible} scheme(s)
        </p>
    `;
    
    data.eligible_schemes.forEach(scheme => {
        const schemeCard = document.createElement('div');
        schemeCard.className = 'scheme-card';
        
        schemeCard.innerHTML = `
            <span class="category">${scheme.category}</span>
            <h3>${scheme.name}</h3>
            <div class="benefit">💰 ${scheme.benefit}</div>
            <button class="btn-roadmap ai-enabled" onclick="showRoadmap('${scheme.id}')">
                🤖 AI-Guided Application →
            </button>
        `;
        schemesList.appendChild(schemeCard);
    });
    
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

async function showRoadmap(schemeId) {
    try {
        const response = await fetch(`${API_BASE_URL}/roadmap/${schemeId}`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch roadmap');
        }
        
        const data = await response.json();
        
        // Open AI assistant for all schemes
        const assistantUrl = `assistant-simple.html?scheme=${schemeId}&url=${encodeURIComponent(data.official_url || '')}`;
        window.open(assistantUrl, '_blank', 'width=900,height=800');
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

function displayRoadmap(data) {
    const modal = document.getElementById('roadmapModal');
    const roadmapContent = document.getElementById('roadmapContent');
    
    let stepsHTML = `
        <h2>${data.scheme_name}</h2>
        <p style="color: #28a745; font-weight: 600; margin: 10px 0 20px 0;">
            💰 ${data.benefit}
        </p>
        <h3 style="margin-bottom: 20px;">Application Steps:</h3>
    `;
    
    data.roadmap.forEach(step => {
        const docs = step.documents.length > 0 
            ? `<div class="documents">📄 Required: ${step.documents.join(', ')}</div>`
            : '';
        
        const location = step.location 
            ? `<div class="documents">📍 Location: ${step.location}</div>`
            : '';
        
        stepsHTML += `
            <div class="roadmap-step">
                <h4>
                    <span class="step-number">${step.step}</span>
                    ${step.title}
                </h4>
                <p><strong>Action:</strong> ${step.action}</p>
                <p><strong>Method:</strong> ${step.method} | <strong>Time:</strong> ${step.time}</p>
                ${docs}
                ${location}
            </div>
        `;
    });
    
    roadmapContent.innerHTML = stepsHTML;
    modal.style.display = 'block';
}

document.querySelector('.close').addEventListener('click', () => {
    document.getElementById('roadmapModal').style.display = 'none';
});

window.addEventListener('click', (e) => {
    const modal = document.getElementById('roadmapModal');
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});
