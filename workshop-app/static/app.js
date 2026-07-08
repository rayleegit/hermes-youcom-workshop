const state = {
  steps: [],
  currentIndex: 0,
  session: {},
  platform: null,
  materials: null,
  expressInfo: null,
  lastResults: null,
  workshopStart: Date.now(),
  timerInterval: null,
  presenterMode: false,
  expressMode: !new URLSearchParams(window.location.search).has("full"),
  deepDives: null,
  agentBuild: null,
  hermesDesktop: null,
  automation: null,
  community: null,
  postEvent: null,
  buildProgress: JSON.parse(localStorage.getItem("agentBuildProgress") || "{}"),
};

const API_STEP_SETUP = {
  "web-search": ["api_setup_env", "api_search_setup", "api_chain_overview"],
  contents: ["api_contents_setup"],
  research: ["api_research_setup"],
  "structured-research": ["api_structured_research"],
};

const GOAL_PRESETS = [
  {
    id: "renewal",
    label: "Renewal",
    goal: "Prepare for renewal QBR — assess expansion risk, adoption signals, contract timing, and retention talking points.",
    job: "When I am preparing for a renewal QBR, I need a risk and expansion brief, so I can enter the conversation with sourced retention and upsell context.",
  },
  {
    id: "outbound",
    label: "Outbound",
    goal: "Prepare outbound sequence — find recent news, credible outreach angle, and priority hooks for first-touch messaging.",
    job: "When I am starting an outbound sequence, I need a sourced prospect brief, so I can personalize first-touch messaging with credible hooks.",
  },
  {
    id: "competitive",
    label: "Competitive",
    goal: "Competitive displacement brief — compare against primary competitor, differentiation angles, and switch triggers.",
    job: "When I am in a competitive deal, I need a displacement brief, so I can counter with sourced differentiation and switch triggers.",
  },
  {
    id: "partner",
    label: "Partner",
    goal: "Partner co-sell prep — joint GTM opportunities, integration signals, and co-selling angles.",
    job: "When I am preparing for a partner call, I need a co-sell brief, so I can align on joint opportunities with sourced context.",
  },
];

const $ = (sel) => document.querySelector(sel);

async function api(path, opts = {}) {
  const res = await fetch(`/api${path}`, {
    headers: { "Content-Type": "application/json" },
    ...opts,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || "Request failed");
  }
  return res.json();
}

function startTimer() {
  state.timerInterval = setInterval(() => {
    const elapsed = Math.floor((Date.now() - state.workshopStart) / 1000);
    const m = Math.floor(elapsed / 60);
    const s = elapsed % 60;
    $("#timer").textContent = `${m}:${String(s).padStart(2, "0")}`;
  }, 1000);
}

function updateBadges(health) {
  const demo = $("#demo-badge");
  const live = $("#live-badge");
  if (health.demo_mode) {
    demo.classList.remove("hidden");
    live.classList.add("hidden");
  } else {
    demo.classList.add("hidden");
    live.classList.remove("hidden");
  }
}

function renderStepList() {
  const list = $("#step-list");
  list.innerHTML = "";
  state.steps.forEach((step, i) => {
    const li = document.createElement("li");
    li.dataset.index = i;
    const done = i < state.currentIndex ? "done" : "";
    const active = i === state.currentIndex ? "active" : "";
    li.className = `${done} ${active}`.trim();
    li.innerHTML = `
      <span class="step-num">${step.number}</span>
      <span class="step-check">${i < state.currentIndex ? "✓" : "○"}</span>
      <span>${step.title}</span>
    `;
    li.addEventListener("click", () => goToStep(i));
    list.appendChild(li);
  });
}

function showSection(id, visible) {
  const el = $(id);
  if (el) el.classList.toggle("hidden", !visible);
}

function renderPlatformSpotlight(step) {
  if (!state.platform) return;
  const { story, youcom_strengths, hermes_strengths, phase_focus } = state.platform;

  $("#story-headline").textContent = story.headline;
  $("#youcom-highlight").textContent = step.youcom_highlight || phase_focus[step.phase]?.youcom || "";
  $("#hermes-highlight").textContent = step.hermes_highlight || phase_focus[step.phase]?.hermes || "";

  const focus = step.platform_focus || phase_focus[step.phase]?.focus || "both";
  const youcomCard = document.querySelector(".youcom-card");
  const hermesCard = document.querySelector(".hermes-card");
  youcomCard.classList.toggle("platform-active", focus === "youcom" || focus === "both");
  hermesCard.classList.toggle("platform-active", focus === "hermes" || focus === "both");
  youcomCard.classList.toggle("platform-dimmed", focus === "hermes");
  hermesCard.classList.toggle("platform-dimmed", focus === "youcom");

  const yf = $("#youcom-features");
  yf.innerHTML = "";
  youcom_strengths.slice(0, 3).forEach((f) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${f.title}</strong> — ${f.detail}`;
    yf.appendChild(li);
  });

  const hf = $("#hermes-features");
  hf.innerHTML = "";
  hermes_strengths.slice(0, 3).forEach((f) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${f.title}</strong> — ${f.detail}`;
    hf.appendChild(li);
  });
}

function renderApiMatrix() {
  if (!state.platform) return;
  const table = $("#api-matrix-table");
  table.innerHTML = "";
  state.platform.api_decision_matrix.forEach((row) => {
    const div = document.createElement("div");
    div.className = "matrix-row";
    div.innerHTML = `
      <div class="matrix-need">${row.need}</div>
      <div class="matrix-api">${row.api}</div>
      <div class="matrix-why">${row.why}</div>
    `;
    table.appendChild(div);
  });
}

function renderLifecycle(activeStage) {
  if (!state.platform) return;
  const track = $("#lifecycle-track");
  track.innerHTML = "";
  state.platform.hermes_lifecycle.forEach((item, i) => {
    const div = document.createElement("div");
    const stages = ["Run", "Integrate", "Govern", "Package", "Pilot"];
    const stageIndex = stages.indexOf(activeStage);
    div.className = `lifecycle-step${i <= stageIndex ? " lifecycle-active" : ""}`;
    div.innerHTML = `<span class="lifecycle-num">${i + 1}</span><strong>${item.stage}</strong><span>${item.detail}</span>`;
    track.appendChild(div);
  });
}

function renderReviewStates() {
  if (!state.platform) return;
  const container = $("#review-states");
  container.innerHTML = "";
  state.platform.review_states.forEach((r) => {
    const div = document.createElement("div");
    div.className = "review-state-card";
    div.innerHTML = `<strong>${r.state}</strong><p>${r.detail}</p><p class="hint">${r.hermes_note}</p>`;
    container.appendChild(div);
  });
}

function renderScorecard() {
  if (!state.platform) return;
  const container = $("#scorecard-fields");
  container.innerHTML = "";
  state.platform.quality_scorecard.forEach((dim) => {
    const div = document.createElement("label");
    div.className = "scorecard-row";
    div.innerHTML = `
      <span class="scorecard-dim">${dim.dimension}</span>
      <span class="scorecard-scale">${dim.scale}</span>
      <select class="score-select" data-dim="${dim.dimension}">
        <option value="">—</option>
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
      </select>
    `;
    container.appendChild(div);
  });
}

function lifecycleStageForStep(step) {
  const map = {
    Setup: "Run", Define: "Run", Discover: "Integrate", Inspect: "Integrate",
    Synthesize: "Integrate", Context: "Integrate", Govern: "Govern",
    Package: "Package", Pilot: "Pilot", Close: "Pilot",
  };
  return map[step.phase] || "Run";
}

function renderStep() {
  const step = state.steps[state.currentIndex];
  if (!step) return;

  $("#phase-tag").textContent = step.phase;
  $("#step-title").textContent = step.title;
  $("#step-number").textContent = step.express_number != null
    ? `Express ${step.express_number + 1} of ${step.express_total}`
    : `Step ${step.number}`;
  $("#step-minutes").textContent = `${step.minutes} min`;
  $("#facilitator-text").textContent = step.facilitator;
  $("#audience-action").textContent = step.audience_action;

  const tp = $("#talking-points");
  tp.innerHTML = "";
  (step.talking_points || []).forEach((p) => {
    const li = document.createElement("li");
    if (p.startsWith("You.com:")) {
      li.className = "tp-youcom";
      li.textContent = p;
    } else if (p.startsWith("Hermes:")) {
      li.className = "tp-hermes";
      li.textContent = p;
    } else {
      li.textContent = p;
    }
    tp.appendChild(li);
  });

  renderPlatformSpotlight(step);

  const id = step.id;
  const express = state.expressMode;
  const governPhases = ["Govern", "Package", "Pilot"];
  showSection("#express-cuts-panel", express && id === "welcome");
  showSection("#post-event-panel", express && (id === "welcome" || id === "wrap-up" || step.show_post_event));
  showSection("#product-checklist-panel", express && (step.show_product_checklist || id === "web-search"));
  showSection("#api-matrix-panel", ["api-matrix", "web-search"].includes(id));
  showSection("#lifecycle-panel", (governPhases.includes(step.phase) || id === "welcome") && !express);
  if (governPhases.includes(step.phase) || id === "welcome") {
    if (!express) renderLifecycle(lifecycleStageForStep(step));
  }

  const showDefine = express
    ? false
    : ["welcome", "choose-job", "define-inputs", "define-output"].includes(id) || state.currentIndex <= 3;
  showSection("#inputs-section", showDefine);
  showSection("#opening-script-panel", id === "welcome" && !express);
  showSection("#schema-panel", id === "define-output" || (express && step.show_schema));
  showSection("#context-section", id === "team-context");
  showSection("#drafts-section", id === "connector-map" && !express);
  showSection("#connector-section", id === "connector-map");
  showSection("#review-section", id === "review-gates" || (express && step.include_review));
  showSection("#scorecard-section", id === "test-three" && !express);
  showSection("#pilot-section", id === "pilot-plan" && !express);
  showSection("#champion-rollout-panel", false);
  showSection("#calendar-prep-panel", false);
  showSection("#closing-script-panel", id === "wrap-up");
  showSection("#community-panel", id === "wrap-up");
  showSection("#source-scoring", id === "inspect-sources" && !express);
  showSection("#api-actions", express
    ? id === "workflow-card"
    : ["web-search", "contents", "research", "structured-research", "workflow-card"].includes(id));
  showSection("#brief-panel", ["review-gates", "workflow-card", "hermes-package", "test-three", "pilot-plan", "wrap-up"].includes(id)
    || (express && step.include_review));
  showSection("#card-panel", ["workflow-card", "hermes-package", "test-three", "pilot-plan", "wrap-up"].includes(id));
  showSection("#agent-build-panel", id === "hermes-package" || !!step.agent_build);
  showSection("#automation-explainer-card", id === "web-search" || id === "hermes-package" || !!step.agent_build);
  if (state.automation) renderAutomationPanel();
  showSection("#hermes-panel", (["hermes-package", "test-three", "pilot-plan", "wrap-up"].includes(id) || step.agent_build) && !step.hermes_live);
  showSection("#hermes-live-panel", !!step.hermes_live);

  applyPresenterMode();

  if (id === "review-gates" || (express && step.include_review)) renderReviewStates();
  if (id === "test-three" && !express) renderScorecard();

  renderApiButtons(step);
  renderStepList();

  $("#prev-btn").disabled = state.currentIndex === 0;
  $("#next-btn").disabled = state.currentIndex === state.steps.length - 1;

  if (["review-gates", "workflow-card", "hermes-package"].includes(id) || (express && step.include_review)) {
    loadBrief();
  }
  if (["workflow-card", "hermes-package"].includes(id)) {
    loadWorkflowCard();
  }
  if (id === "wrap-up") {
    loadBrief();
    loadWorkflowCard();
    loadHermesPrompt();
    loadAgentBuild();
    loadCommunity();
    renderPostEventPanel();
  }
  if (id === "welcome" && state.expressMode) {
    renderPostEventPanel();
  }
  if (id === "hermes-package" || step.agent_build) {
    loadAgentBuild();
    loadHermesPrompt();
  }
  if (step.hermes_live) {
    loadHermesLiveRun();
  }

  renderLearnMore(step);
  renderInlineQuickRefs(id, step);
}

function applyPresenterMode() {
  const hide = state.presenterMode;
  showSection("#facilitator-panel", !hide);
  showSection("#opening-script-panel", !hide && state.steps[state.currentIndex]?.id === "welcome");
  document.body.classList.toggle("presenter-mode", hide);
  $("#presenter-toggle").textContent = hide ? "Show Facilitator Notes" : "Presenter Mode";
  $("#presenter-toggle").classList.toggle("btn-primary", hide);
}

function renderBlock(block, compact = false) {
  const wrap = document.createElement("div");
  wrap.className = "deep-dive-block";

  if (block.type === "text") {
    const p = document.createElement("p");
    p.className = "deep-dive-text";
    p.textContent = block.content;
    wrap.appendChild(p);
  } else if (block.type === "list") {
    const ul = document.createElement("ul");
    ul.className = "deep-dive-list";
    (block.items || []).forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      ul.appendChild(li);
    });
    wrap.appendChild(ul);
  } else if (block.type === "table") {
    const table = document.createElement("table");
    table.className = "deep-dive-table";
    const thead = document.createElement("thead");
    const hr = document.createElement("tr");
    (block.headers || []).forEach((h) => {
      const th = document.createElement("th");
      th.textContent = h;
      hr.appendChild(th);
    });
    thead.appendChild(hr);
    table.appendChild(thead);
    const tbody = document.createElement("tbody");
    (block.rows || []).forEach((row) => {
      const tr = document.createElement("tr");
      row.forEach((cell) => {
        const td = document.createElement("td");
        td.textContent = cell;
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    wrap.appendChild(table);
  } else if (block.type === "code") {
    const head = document.createElement("div");
    head.className = "deep-dive-code-head";
    if (block.label) {
      const label = document.createElement("span");
      label.className = "deep-dive-code-label";
      label.textContent = block.label;
      head.appendChild(label);
    }
    if (block.copy !== false) {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "btn btn-ghost btn-sm";
      btn.textContent = "Copy";
      btn.addEventListener("click", () => copyText(block.content));
      head.appendChild(btn);
    }
    wrap.appendChild(head);
    const pre = document.createElement("pre");
    pre.className = compact ? "deep-dive-code compact" : "deep-dive-code";
    pre.textContent = block.content;
    wrap.appendChild(pre);
  } else if (block.type === "links") {
    const ul = document.createElement("ul");
    ul.className = "deep-dive-links";
    (block.items || []).forEach((item) => {
      const li = document.createElement("li");
      if (item.url) {
        const a = document.createElement("a");
        a.href = item.url;
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.textContent = item.label;
        li.appendChild(a);
      } else if (item.path) {
        li.innerHTML = `<code>${escapeHtml(item.path)}</code> — ${escapeHtml(item.label)}`;
      } else {
        li.textContent = item.label || "";
      }
      ul.appendChild(li);
    });
    wrap.appendChild(ul);
  }

  return wrap;
}

function renderDeepDiveTopic(topicId, { open = false, compact = false } = {}) {
  const dive = state.deepDives?.dives?.[topicId];
  if (!dive) return null;

  const details = document.createElement("details");
  details.className = "deep-dive-topic";
  if (open) details.open = true;

  const summary = document.createElement("summary");
  summary.textContent = dive.title;
  details.appendChild(summary);

  const body = document.createElement("div");
  body.className = "deep-dive-body";
  if (dive.intro) {
    const intro = document.createElement("p");
    intro.className = "deep-dive-intro";
    intro.textContent = dive.intro;
    body.appendChild(intro);
  }
  (dive.blocks || []).forEach((block) => {
    body.appendChild(renderBlock(block, compact));
  });
  details.appendChild(body);
  return details;
}

function topicsForStep(step) {
  const topics = [...(state.deepDives?.step_map?.[step.id] || [])];
  if (step.include_review && !topics.includes("review_gates")) {
    topics.push("review_gates");
  }
  if (step.use_full_chain) {
    [
      "api_setup_env",
      "api_chain_overview",
      "api_search_setup",
      "api_contents_setup",
      "api_research_setup",
      "api_structured_research",
    ].forEach((topicId) => {
      if (!topics.includes(topicId)) topics.push(topicId);
    });
  }
  if (step.hermes_live && !topics.includes("hermes_live_setup")) {
    topics.push("hermes_live_setup");
  }
  if (step.agent_build && !topics.includes("hermes_automation_loop")) {
    topics.unshift("hermes_automation_loop");
  }
  if (step.agent_build && !topics.includes("agent_build_e2e")) {
    topics.unshift("agent_build_e2e");
  }
  if (step.agent_build && !topics.includes("hermes_desktop_setup")) {
    topics.unshift("hermes_desktop_setup");
  }
  if (step.show_schema && !topics.includes("output_schema_guide")) {
    topics.push("output_schema_guide");
  }
  return topics;
}

function renderLearnMore(step) {
  const panel = $("#learn-more-panel");
  const container = $("#learn-more-content");
  if (!panel || !container || !state.deepDives || !step) return;

  const topics = topicsForStep(step);
  container.innerHTML = "";
  if (!topics.length) {
    showSection("#learn-more-panel", false);
    return;
  }

  topics.forEach((topicId, i) => {
    const node = renderDeepDiveTopic(topicId, { open: i === 0 });
    if (node) container.appendChild(node);
  });
  showSection("#learn-more-panel", true);
}

function renderInlineQuickRefs(stepId, step) {
  const connectorRef = $("#connector-quick-ref");
  if (connectorRef) {
    connectorRef.innerHTML = "";
    if (stepId === "connector-map") {
      ["connector_map"].forEach((topicId) => {
        const dive = state.deepDives?.dives?.[topicId];
        if (!dive) return;
        (dive.blocks || []).forEach((block) => {
          if (block.type === "table" || block.type === "code") {
            connectorRef.appendChild(renderBlock(block, true));
          }
        });
      });
    }
  }

  const reviewRef = $("#review-quick-ref");
  if (reviewRef) {
    reviewRef.innerHTML = "";
    if (stepId === "review-gates" || step.include_review) {
      const dive = state.deepDives?.dives?.review_gates;
      if (dive) {
        (dive.blocks || []).forEach((block) => reviewRef.appendChild(renderBlock(block, true)));
      }
    }
  }

  const apiRef = $("#api-setup-quick-ref");
  const apiDrilldown = $("#api-setup-drilldown");
  if (apiRef && apiDrilldown) {
    apiRef.innerHTML = "";
    const setupTopics = API_STEP_SETUP[stepId]
      || (state.expressMode && stepId === "web-search"
        ? ["api_setup_env", "api_search_setup", "api_contents_setup", "api_research_setup", "api_chain_overview"]
        : null)
      || (["web-search", "contents", "research", "structured-research"].includes(stepId)
        ? API_STEP_SETUP[stepId]
        : null);

    if (setupTopics?.length) {
      setupTopics.forEach((topicId) => {
        const node = renderDeepDiveTopic(topicId, { compact: true });
        if (node) {
          node.open = topicId === setupTopics[0];
          apiRef.appendChild(node);
        }
      });
      apiDrilldown.classList.remove("hidden");
    } else {
      apiDrilldown.classList.add("hidden");
    }
  }
}

function renderProductChecklist() {
  const list = $("#product-checklist");
  if (!list || !state.platform?.youcom_products) return;
  list.innerHTML = "";
  state.platform.youcom_products.forEach((p) => {
    const li = document.createElement("li");
    li.dataset.productId = p.id;
    li.innerHTML = `<strong>☐ ${p.name}</strong>${p.job}<br><span>${p.where}</span>`;
    li.addEventListener("click", () => {
      li.classList.toggle("covered");
      li.querySelector("strong").textContent = li.classList.contains("covered")
        ? `✓ ${p.name}` : `☐ ${p.name}`;
    });
    list.appendChild(li);
  });
}

function renderFullChainResults(data) {
  const summary = $("#results-summary");
  summary.innerHTML = "";
  if (data.demo_mode) {
    const note = document.createElement("p");
    note.className = "hint";
    note.textContent = "⚠ Demo mode — sample data for teaching";
    summary.appendChild(note);
  }
  if (data.notes?.length) {
    const note = document.createElement("p");
    note.className = "hint";
    note.textContent = data.notes.join(" · ");
    summary.appendChild(note);
  }
  if (data.skipped?.length) {
    const note = document.createElement("p");
    note.className = "hint";
    note.textContent = `Optional steps skipped: ${data.skipped.join("; ")}`;
    summary.appendChild(note);
  }
  const sections = [
    { title: "1. Web Search API", body: `${(data.search_summary || []).length} results — inspect titles, URLs, snippets below` },
    { title: "2. Contents API", body: `${data.contents_count || 0} pages fetched as markdown` },
    { title: "3. Research API", body: data.research_preview || "" },
    { title: "4. Structured Research (output_schema)", body: data.structured_preview || "" },
    { title: "5. Finance Research API", body: data.finance_preview || "" },
  ];
  sections.forEach((s) => {
    const div = document.createElement("div");
    div.className = "source-item";
    div.innerHTML = `<div class="source-info"><div class="source-title">${s.title}</div><div class="source-snippet">${escapeHtml(s.body)}</div></div>`;
    summary.appendChild(div);
  });
  if (data.search_summary) {
    data.search_summary.slice(0, 3).forEach((item) => {
      const div = document.createElement("div");
      div.className = "source-item";
      div.innerHTML = `<div class="source-info"><div class="source-title">[Search] ${item.title}</div><div class="source-url">${item.url}</div></div>`;
      summary.appendChild(div);
    });
  }
  $("#results-raw").textContent = JSON.stringify(data, null, 2);
}

async function runFullChain() {
  const btn = $("#full-chain-btn");
  const orig = btn.textContent;
  btn.disabled = true;
  const waitHint = state.expressMode
    ? "Running core chain (Search → Contents → Research)…"
    : "Running full chain… Finance Research may take 2–5 min when included.";
  btn.innerHTML = `<span class="loading"></span>${waitHint}`;
  try {
    const data = await api("/run/full-chain", {
      method: "POST",
      body: JSON.stringify({
        include_structured: !state.expressMode,
        include_finance: !state.expressMode,
      }),
    });
    state.lastResults = data;
    renderFullChainResults(data);
    if (data.search_summary) {
      renderSourceScoring(data.search_summary);
      showSection("#source-scoring", !state.expressMode);
    }
    showSection("#results-panel", true);
    let msg = `Chain complete:\n${data.steps_run.join(" → ")}`;
    if (data.skipped?.length) {
      msg += `\n\nSkipped:\n${data.skipped.join("\n")}`;
    }
    if (state.expressMode) {
      msg += "\n\n60-min track: run **Finance Research (Optional)** separately if you want financial context.";
    }
    alert(msg);
  } catch (err) {
    alert(`Chain error: ${err.message}`);
  } finally {
    btn.disabled = false;
    btn.textContent = orig;
  }
}

async function downloadPilotTemplate() {
  const data = await api("/export-all");
  const company = state.session.company || "account";
  const slug = company.toLowerCase().replace(/\s+/g, "-");
  downloadMarkdown(`${slug}-team-rollout-template.md`, data.pilot_plan);
}

async function downloadAllArtifacts() {
  const data = await api("/export-all");
  const company = state.session.company || "account";
  const slug = company.toLowerCase().replace(/\s+/g, "-");
  downloadMarkdown(`${slug}-account-action-brief.md`, data.brief);
  setTimeout(() => downloadMarkdown(`${slug}-workflow-card.md`, data.workflow_card), 300);
  setTimeout(() => downloadMarkdown(`${slug}-agent-build-kit.md`, data.agent_kit), 600);
  setTimeout(() => downloadMarkdown(`${slug}-hermes-prompt.md`, data.hermes_prompt), 900);
  setTimeout(() => downloadMarkdown(`${slug}-pilot-plan.md`, data.pilot_plan), 1200);
  setTimeout(() => downloadMarkdown(`${slug}-community-playbook.md`, data.community_playbook), 1500);
  setTimeout(() => downloadMarkdown(`${slug}-team-rollout-template.md`, data.pilot_plan), 1800);
  setTimeout(() => downloadMarkdown(`${slug}-hermes-desktop-setup.md`, data.hermes_desktop_setup), 2100);
}

function renderHermesDesktopPanel() {
  const data = state.hermesDesktop;
  if (!data) return;

  const intro = $("#hermes-desktop-intro");
  if (intro) {
    intro.textContent = `${data.subtitle} Skills install to ${data.skills_dest}. See ${data.docs}.`;
  }

  const skillsEl = $("#hermes-desktop-skills");
  if (skillsEl) {
    skillsEl.innerHTML = "";
    (data.skills || []).forEach((skill) => {
      const card = document.createElement("div");
      card.className = "hermes-skill-chip";
      card.innerHTML = `<strong>${escapeHtml(skill.name)}</strong><span>${escapeHtml(skill.summary)}</span>`;
      skillsEl.appendChild(card);
    });
  }

  const installCmd = $("#hermes-install-cmd");
  if (installCmd) installCmd.textContent = data.install_commands?.script || "";

  const testCmd = $("#hermes-test-cmd");
  if (testCmd) testCmd.textContent = data.test_command || "";

  const mp = $("#meeting-prep-test-cmd");
  if (mp && data.meeting_prep_test_command) mp.textContent = data.meeting_prep_test_command;

  const checklist = $("#hermes-desktop-checklist");
  if (checklist) {
    checklist.innerHTML = "";
    (data.setup_checklist || []).forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      checklist.appendChild(li);
    });
  }
}

async function downloadHermesSkillPack() {
  const company = (state.session.company || "workshop").toLowerCase().replace(/\s+/g, "-");
  const res = await fetch("/api/hermes-desktop/download");
  if (!res.ok) throw new Error("Skill pack download failed");
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${company}-hermes-skill-pack.zip`;
  a.click();
  URL.revokeObjectURL(url);
}

function loadPilotForm(session) {
  const t = state.materials?.pilot_plan_template || {};
  const p = session.pilot_plan || {};
  $("#pilot-owner").value = p.workflow_owner || session.workflow_owner || "";
  $("#pilot-users").value = p.pilot_users || t.pilot_users || "5";
  $("#pilot-accounts").value = p.pilot_accounts || t.pilot_accounts || "20";
  $("#pilot-week0").value = p.week0_tasks || t.week0_tasks || "";
  $("#pilot-week1").value = p.week1_goal || t.week1_goal || "";
  $("#pilot-week2").value = p.week2_goal || t.week2_goal || "";
  $("#pilot-metrics").value = p.success_metrics || t.success_metrics || "";
  $("#pilot-expand").value = p.expand_criteria || t.expand_criteria || "";
}

async function savePilotPlan() {
  await api("/session", {
    method: "PATCH",
    body: JSON.stringify({
      workflow_owner: $("#pilot-owner").value,
      pilot_plan: {
        workflow_owner: $("#pilot-owner").value,
        pilot_users: $("#pilot-users").value,
        pilot_accounts: $("#pilot-accounts").value,
        week0_tasks: $("#pilot-week0").value,
        week1_goal: $("#pilot-week1").value,
        week2_goal: $("#pilot-week2").value,
        success_metrics: $("#pilot-metrics").value,
        expand_criteria: $("#pilot-expand").value,
      },
    }),
  });
  state.session = await api("/session");
  alert("Pilot plan saved.");
}

function renderApiButtons(step) {
  const container = $("#api-buttons");
  const hint = $("#api-hint");
  const fullChainBtn = $("#full-chain-btn");
  container.innerHTML = "";

  if (state.expressMode && step.id === "web-search") {
    fullChainBtn.classList.add("hidden");
    hint.textContent =
      "Walk You.com APIs in the platform playground: https://you.com/platform — slides 5–9 are the script.";
    showSection("#results-panel", false);
    return;
  }
  fullChainBtn.classList.toggle("hidden", state.expressMode && step.id !== "web-search");

  fullChainBtn.classList.toggle("hidden", state.expressMode && step.id !== "web-search");

  const actions = {
    search: { label: "Run Web Search", endpoint: "/run/search", method: "POST" },
    contents: { label: "Run Contents", endpoint: "/run/contents", method: "POST" },
    research: { label: "Run Research", endpoint: "/run/research", method: "POST" },
    research_structured: { label: "Run Structured Research", endpoint: "/run/research-structured", method: "POST" },
    generate_card: { label: "Generate Workflow Card", action: "generate_card" },
  };

  const action = step.api_action;
  showSection("#results-panel", !!action && action !== "generate_card");

  if (!action) {
    if (["web-search", "contents", "research", "structured-research"].includes(step.id)) {
      hint.textContent = state.session.demo_mode
        ? "Use Run Full Demo Chain below, or run individual API buttons when on the matching step."
        : "Run individual APIs or use Run Full Demo Chain to populate all results.";
    } else {
      hint.textContent = "";
    }
    return;
  }

  if (action === "generate_card") {
    const btn = document.createElement("button");
    btn.className = "btn btn-primary";
    btn.textContent = actions.generate_card.label;
    btn.addEventListener("click", () => {
      loadWorkflowCard();
      goToStep(state.currentIndex + 1);
    });
    container.appendChild(btn);
    hint.textContent = "Generates the workflow card from your session data.";
    return;
  }

  const cfg = actions[action];
  if (!cfg) return;

  const btn = document.createElement("button");
  btn.className = "btn btn-primary";
  btn.textContent = cfg.label;
  btn.addEventListener("click", () => runApi(cfg.endpoint, btn));
  container.appendChild(btn);

  if (action === "search") {
    const domainBtn = document.createElement("button");
    domainBtn.className = "btn btn-secondary";
    domainBtn.textContent = "Search (Official Domain Only)";
    domainBtn.addEventListener("click", () => {
      const domain = $("#website").value.replace(/^https?:\/\//, "").split("/")[0];
      runApi("/run/search", domainBtn, { include_domains: domain ? [domain] : [] });
    });
    container.appendChild(domainBtn);
  }

  if (action === "research") {
    const financeBtn = document.createElement("button");
    financeBtn.className = "btn btn-secondary";
    financeBtn.textContent = "Run Finance Research (Optional, 2–5 min)";
    financeBtn.addEventListener("click", () => runApi("/run/finance-research", financeBtn));
    container.appendChild(financeBtn);
  }

  hint.textContent = state.session.demo_mode
    ? "Demo mode: sample You.com responses. Set YDC_API_KEY for live calls. Hermes packaging works the same either way."
    : "Live You.com API mode. Results feed into the Hermes workflow card and brief.";
}

async function runApi(endpoint, btn, body = {}) {
  const orig = btn.textContent;
  btn.disabled = true;
  const loading = endpoint.includes("finance-research")
    ? "Finance Research running (2–5 min)…"
    : "Running…";
  btn.innerHTML = `<span class="loading"></span>${loading}`;
  try {
    const data = await api(endpoint, { method: "POST", body: JSON.stringify(body) });
    state.lastResults = data;
    renderResults(data);
    if (endpoint === "/run/search" && data.summary) {
      renderSourceScoring(data.summary);
    }
    showSection("#results-panel", true);
  } catch (err) {
    alert(`API error: ${err.message}`);
  } finally {
    btn.disabled = false;
    btn.textContent = orig;
  }
}

function renderResults(data) {
  const summary = $("#results-summary");
  const raw = $("#results-raw");
  summary.innerHTML = "";
  raw.textContent = JSON.stringify(data.results || data, null, 2);

  if (data.summary) {
    data.summary.forEach((item) => {
      const div = document.createElement("div");
      div.className = "source-item";
      div.innerHTML = `
        <div class="source-info">
          <div class="source-title">[${item.type}] ${item.title}</div>
          <div class="source-url">${item.url}</div>
          ${item.snippet ? `<div class="source-snippet">${item.snippet}</div>` : ""}
          ${item.page_age ? `<div class="source-snippet">Freshness: ${item.page_age}</div>` : ""}
        </div>
      `;
      summary.appendChild(div);
    });
  } else if (data.results?.output) {
    const out = data.results.output;
    const div = document.createElement("div");
    div.className = "source-item";
    let content = out.content;
    if (typeof content === "string" && content.startsWith("{")) {
      try { content = JSON.stringify(JSON.parse(content), null, 2); } catch {}
    }
    div.innerHTML = `<pre class="markdown-preview" style="max-height:300px">${escapeHtml(String(content).slice(0, 3000))}</pre>`;
    summary.appendChild(div);
    if (out.sources?.length) {
      out.sources.forEach((s) => {
        const sdiv = document.createElement("div");
        sdiv.className = "source-item";
        sdiv.innerHTML = `<div class="source-info"><div class="source-title">${s.title || "Source"}</div><div class="source-url">${s.url || ""}</div></div>`;
        summary.appendChild(sdiv);
      });
    }
  } else if (data.results?.results) {
    const pages = data.results.results;
    pages.forEach((p) => {
      const div = document.createElement("div");
      div.className = "source-item";
      div.innerHTML = `
        <div class="source-info">
          <div class="source-title">${p.title || p.url}</div>
          <div class="source-url">${p.url}</div>
          <div class="source-snippet">${(p.markdown || "").slice(0, 400)}…</div>
        </div>
      `;
      summary.appendChild(div);
    });
  }

  if (data.demo_mode) {
    const note = document.createElement("p");
    note.className = "hint";
    note.textContent = "⚠ Demo mode — sample data for teaching";
    summary.prepend(note);
  }
}

function renderSourceScoring(summary) {
  const list = $("#source-score-list");
  list.innerHTML = "";
  summary.forEach((item, i) => {
    const div = document.createElement("div");
    div.className = "source-item";
    div.innerHTML = `
      <div class="source-info">
        <div class="source-title">${item.title}</div>
        <div class="source-url">${item.url}</div>
      </div>
      <select class="score-select" data-url="${item.url}">
        <option value="">Score</option>
        <option value="3">3 — Strong</option>
        <option value="2">2 — Usable</option>
        <option value="1">1 — Weak</option>
        <option value="0">0 — Do not use</option>
      </select>
    `;
    list.appendChild(div);
  });
  list.querySelectorAll(".score-select").forEach((sel) => {
    sel.addEventListener("change", saveSourceScores);
  });
}

async function saveSourceScores() {
  const scores = {};
  document.querySelectorAll(".score-select").forEach((sel) => {
    if (sel.value) scores[sel.dataset.url] = parseInt(sel.value, 10);
  });
  const urls = Object.keys(scores).filter((u) => scores[u] >= 2);
  await api("/session", { method: "PATCH", body: JSON.stringify({ source_scores: scores, selected_urls: urls }) });
}

async function saveInputs() {
  await api("/session", {
    method: "PATCH",
    body: JSON.stringify({
      company: $("#company").value,
      website: $("#website").value,
      workflow_goal: $("#workflow-goal").value,
      job: $("#job").value,
      primary_user: $("#primary-user").value,
      workflow_owner: $("#workflow-owner").value,
    }),
  });
  state.session = await api("/session");
  syncGoalPresetHighlight();
}

function renderGoalPresets() {
  const container = $("#goal-presets");
  if (!container) return;
  container.innerHTML = "";
  GOAL_PRESETS.forEach((preset) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "goal-preset-btn";
    btn.dataset.presetId = preset.id;
    btn.textContent = preset.label;
    btn.title = preset.goal;
    btn.addEventListener("click", () => applyGoalPreset(preset.id));
    container.appendChild(btn);
  });
  syncGoalPresetHighlight();
}

function applyGoalPreset(presetId) {
  const preset = GOAL_PRESETS.find((p) => p.id === presetId);
  if (!preset) return;
  $("#workflow-goal").value = preset.goal;
  $("#job").value = preset.job;
  syncGoalPresetHighlight();
  const saveBtn = $("#save-inputs-btn");
  if (saveBtn) {
    saveBtn.textContent = "Save Inputs (goal updated)";
    setTimeout(() => {
      saveBtn.textContent = "Save Inputs";
    }, 2500);
  }
}

function syncGoalPresetHighlight() {
  const current = ($("#workflow-goal")?.value || "").trim();
  document.querySelectorAll(".goal-preset-btn").forEach((btn) => {
    const preset = GOAL_PRESETS.find((p) => p.id === btn.dataset.presetId);
    btn.classList.toggle("active", !!preset && preset.goal === current);
  });
}

async function saveContext() {
  await api("/session", {
    method: "PATCH",
    body: JSON.stringify({ internal_context: $("#internal-context").value }),
  });
}

async function saveConnectors() {
  await api("/session", {
    method: "PATCH",
    body: JSON.stringify({
      read_tools: $("#read-tools").value,
      draft_tools: $("#draft-tools").value,
      blocked_tools: $("#blocked-tools").value,
    }),
  });
}

async function saveReviewStatus() {
  await api("/session", {
    method: "PATCH",
    body: JSON.stringify({ review_status: $("#review-status").value }),
  });
}

async function loadBrief() {
  const data = await api("/brief");
  $("#brief-content").textContent = data.markdown;
}

async function loadWorkflowCard() {
  const data = await api("/workflow-card");
  $("#card-content").textContent = data.markdown;
  showSection("#card-panel", true);
}

async function loadHermesLiveRun() {
  const data = await api("/hermes-live-run");
  $("#hermes-setup-checklist").textContent = data.setup_checklist;
  $("#hermes-run-command").textContent = data.run_command;
  $("#hermes-evidence-bundle").textContent = data.evidence_bundle;
}

async function loadHermesPrompt() {
  const data = await api("/hermes-prompt");
  $("#hermes-content").textContent = data.prompt;
}

function saveBuildProgress() {
  localStorage.setItem("agentBuildProgress", JSON.stringify(state.buildProgress));
}

function updateBuildProgressUI() {
  const total = state.agentBuild?.steps?.length || 6;
  const done = Object.values(state.buildProgress).filter(Boolean).length;
  const pct = total ? Math.round((done / total) * 100) : 0;
  const bar = $("#build-progress-bar");
  const label = $("#build-progress-label");
  if (bar) bar.style.width = `${pct}%`;
  if (label) label.textContent = `${done} / ${total} complete`;
}

function renderAgentBuildLab() {
  const data = state.agentBuild;
  const container = $("#agent-build-steps");
  if (!data || !container) return;

  const step = state.steps[state.currentIndex];
  const inRoomOnly = step?.agent_build_in_room_only;
  const scope = $("#agent-build-scope");
  if (scope) {
    if (inRoomOnly) {
      scope.innerHTML =
        `<strong>60-min workshop:</strong> complete steps marked <span class="badge-in-room">Live</span> in the room (~${data.in_room_minutes || 13} min). ` +
        `Steps marked <span class="badge-async">After event</span> → <code>AGENT-BUILD-GUIDE.md</code>.`;
    } else {
      scope.innerHTML =
        `<strong>60-min workshop:</strong> all ${data.steps?.length || 6} steps are <span class="badge-in-room">Live</span> in the room (~${data.in_room_minutes || data.total_minutes || 21} min). ` +
        "Use slides 12–15 for copy-paste blocks.";
    }
  }
  $("#agent-build-subtitle").textContent = data.title || "Agent Build Lab";
  $("#agent-fallback-note").textContent = data.fallback_note || "";

  container.innerHTML = "";
  data.steps.forEach((step) => {
    const details = document.createElement("details");
    details.className = `build-step${state.buildProgress[step.id] ? " build-step-done" : ""}`;
    if (state.buildProgress[step.id]) details.open = false;

    const summary = document.createElement("summary");
    const check = state.buildProgress[step.id] ? "✓" : "○";
    const roomBadge = step.in_room
      ? '<span class="badge-in-room">Live</span>'
      : '<span class="badge-async">After event</span>';
    summary.innerHTML = `<span class="build-step-check">${check}</span> <span class="build-step-title">${escapeHtml(step.title)}</span> ${roomBadge} <span class="build-step-mins">~${step.minutes} min</span>`;
    details.appendChild(summary);

    const body = document.createElement("div");
    body.className = "build-step-body";

    const p = document.createElement("p");
    p.className = "deep-dive-text";
    p.textContent = step.summary;
    body.appendChild(p);

    const ul = document.createElement("ul");
    ul.className = "deep-dive-list";
    (step.instructions || []).forEach((line) => {
      const li = document.createElement("li");
      li.textContent = line;
      ul.appendChild(li);
    });
    body.appendChild(ul);

    if (step.copy_content) {
      const head = document.createElement("div");
      head.className = "deep-dive-code-head";
      head.innerHTML = `<span class="deep-dive-code-label">Copy into Hermes</span>`;
      const copyBtn = document.createElement("button");
      copyBtn.type = "button";
      copyBtn.className = "btn btn-ghost btn-sm";
      copyBtn.textContent = "Copy";
      copyBtn.addEventListener("click", () => copyText(step.copy_content));
      head.appendChild(copyBtn);
      body.appendChild(head);
      const pre = document.createElement("pre");
      pre.className = "deep-dive-code compact";
      pre.textContent = step.copy_content;
      body.appendChild(pre);
    }

    const verify = document.createElement("p");
    verify.className = "build-verify";
    verify.innerHTML = `<strong>Verify:</strong> ${escapeHtml(step.verify)}`;
    body.appendChild(verify);

    const doneBtn = document.createElement("button");
    doneBtn.type = "button";
    doneBtn.className = `btn btn-sm ${state.buildProgress[step.id] ? "btn-ghost" : "btn-secondary"}`;
    doneBtn.textContent = state.buildProgress[step.id] ? "Mark incomplete" : "Mark complete";
    doneBtn.addEventListener("click", () => {
      state.buildProgress[step.id] = !state.buildProgress[step.id];
      saveBuildProgress();
      renderAgentBuildLab();
      renderAgentVerifyList();
      updateBuildProgressUI();
    });
    body.appendChild(doneBtn);

    details.appendChild(body);
    container.appendChild(details);
  });

  renderAgentVerifyList();
  updateBuildProgressUI();
}

function renderAgentVerifyList() {
  const list = $("#agent-verify-list");
  if (!list || !state.agentBuild) return;
  list.innerHTML = "";
  state.agentBuild.verification_checklist.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });
}

function renderAutomationPanel() {
  const data = state.automation;
  if (!data) return;
  const summary = $("#automation-summary");
  if (summary) summary.textContent = data.summary || "";
  const loop = $("#automation-loop");
  if (loop) {
    loop.innerHTML = "";
    (data.loop || []).forEach((item) => {
      const li = document.createElement("li");
      li.innerHTML = `<strong>${escapeHtml(item.step)}</strong> — ${escapeHtml(item.detail)}`;
      loop.appendChild(li);
    });
  }
  const does = $("#automation-does");
  if (does) {
    does.innerHTML = "";
    (data.automated || []).forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      does.appendChild(li);
    });
  }
  const human = $("#automation-human");
  if (human) {
    human.innerHTML = "";
    (data.human || []).forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      human.appendChild(li);
    });
  }
}

async function loadAgentBuild() {
  const [build, live, desktop, automation] = await Promise.all([
    api("/agent-build"),
    api("/hermes-live-run").catch(() => ({ evidence_bundle: "" })),
    api("/hermes-desktop").catch(() => null),
    api("/automation").catch(() => null),
  ]);
  state.agentBuild = build;
  state.hermesDesktop = desktop;
  state.automation = automation;
  $("#agent-evidence-bundle").textContent = live.evidence_bundle || "";
  renderAgentBuildLab();
  renderHermesDesktopPanel();
  renderAutomationPanel();
}

async function downloadAgentKit() {
  const data = await api("/export-all");
  const company = state.session.company || "account";
  const slug = company.toLowerCase().replace(/\s+/g, "-");
  downloadMarkdown(`${slug}-agent-build-kit.md`, data.agent_kit);
}

async function loadCommunity() {
  const [community, desktop] = await Promise.all([
    api("/community"),
    state.hermesDesktop ? Promise.resolve(state.hermesDesktop) : api("/hermes-desktop").catch(() => null),
  ]);
  state.community = community;
  if (desktop) state.hermesDesktop = desktop;
  renderCommunityPanel();
  const mp = $("#meeting-prep-test-cmd");
  if (mp && desktop?.meeting_prep_test_command) {
    mp.textContent = desktop.meeting_prep_test_command;
  }
}

function renderCommunityPanel() {
  const data = state.community;
  if (!data) return;

  const cfg = data.config || {};
  const intro = $("#community-intro");
  if (intro && data.discord_intro_instructions) {
    intro.textContent = data.discord_intro_instructions;
  }
  const introPre = $("#discord-intro-template");
  if (introPre) introPre.textContent = data.discord_intro_template || "";
  const introInst = $("#discord-intro-instructions");
  if (introInst) {
    introInst.textContent =
      "Post in #introductions (or the welcome channel). Mention you joined from the Account Action Brief workshop.";
  }

  const links = $("#community-links");
  if (links) {
    links.innerHTML = "";
    if (cfg.name) {
      const h = document.createElement("p");
      h.innerHTML = `<strong>${escapeHtml(cfg.name)}</strong>`;
      links.appendChild(h);
    }
    const discord = cfg.discord_url || cfg.join_url;
    const linkItems = [
      ["Join You.com Discord", discord],
      ["Community chat", cfg.slack_url],
      ["Hermes org", cfg.hermes_org, false],
      ["Contact", cfg.contact, false],
    ];
    linkItems.forEach(([label, value, isUrl = true]) => {
      if (!value) return;
      const p = document.createElement("p");
      if (isUrl && value.startsWith("http")) {
        p.innerHTML = `<a href="${escapeHtml(value)}" target="_blank" rel="noopener noreferrer">${escapeHtml(label)} →</a>`;
      } else {
        p.innerHTML = `<strong>${escapeHtml(label)}:</strong> ${escapeHtml(value)}`;
      }
      links.appendChild(p);
    });
    if (!data.configured) {
      const note = document.createElement("p");
      note.className = "hint";
      note.textContent =
        "Co-hosts: set COMMUNITY_JOIN_URL and related vars in workshop-app/.env to show live links.";
      links.appendChild(note);
    }
  }

  const onboarding = $("#community-onboarding");
  if (onboarding) {
    onboarding.innerHTML = "";
    (data.member_onboarding || []).forEach((step) => {
      const li = document.createElement("li");
      li.textContent = step;
      onboarding.appendChild(li);
    });
  }

  const challenges = $("#community-challenges");
  if (challenges) {
    challenges.innerHTML = "";
    (data.challenges || []).forEach((c) => {
      const div = document.createElement("div");
      div.className = "challenge-item";
      div.innerHTML = `<strong>${escapeHtml(c.week)} — ${escapeHtml(c.title)}</strong><p>${escapeHtml(c.task)}</p>`;
      challenges.appendChild(div);
    });
  }

  const apiPaths = $("#community-api-paths");
  if (apiPaths) {
    apiPaths.innerHTML = "";
    (data.api_paths || []).forEach((p) => {
      const div = document.createElement("div");
      div.className = "source-item";
      div.innerHTML = `<div class="source-info"><div class="source-title">${escapeHtml(p.path)}</div><div class="source-snippet">${escapeHtml(p.detail)}</div></div>`;
      apiPaths.appendChild(div);
    });
  }

  const model = data.hermes_messaging_model;
  if (model && $("#community-messaging-model")) {
    $("#community-messaging-model").textContent = model.summary || "";
  }
  if ($("#broadcast-skill")) $("#broadcast-skill").textContent = data.broadcast_skill_instruction || "";
  if ($("#broadcast-command")) $("#broadcast-command").textContent = data.broadcast_run_command || "";
}

async function downloadCommunityPlaybook() {
  const data = await api("/export-all");
  const slug = (state.session.company || "community").toLowerCase().replace(/\s+/g, "-");
  downloadMarkdown(`${slug}-community-playbook.md`, data.community_playbook);
}

function goToStep(index) {
  state.currentIndex = index;
  renderStep();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function escapeHtml(str) {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function copyText(text) {
  navigator.clipboard.writeText(text).then(() => alert("Copied to clipboard"));
}

function downloadMarkdown(filename, content) {
  const blob = new Blob([content], { type: "text/markdown" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = filename;
  a.click();
}

async function loadSteps() {
  const path = state.expressMode ? "/steps?express=true" : "/steps";
  state.steps = await api(path);
  if (state.expressMode) {
    state.expressInfo = await api("/express-track");
    renderPostEventPanel();
  }
  state.currentIndex = 0;
  renderExpressCuts();
  updateExpressToggle();
  renderStepList();
  renderStep();
}

function renderExpressCuts() {
  const list = $("#express-cuts-list");
  if (!list || !state.expressInfo) return;
  list.innerHTML = "";
  state.expressInfo.cuts.forEach((cut) => {
    const li = document.createElement("li");
    li.textContent = cut;
    list.appendChild(li);
  });
}

function updateExpressToggle() {
  const btn = $("#express-toggle");
  if (state.expressMode) {
    btn.textContent = "Deep Dive Track (90 min)";
    btn.classList.add("btn-primary");
    document.querySelector(".subtitle").textContent =
      "60-MIN LIVE — You.com evidence + Hermes agent start · depth after the event";
  } else {
    btn.textContent = "60-Min Live Workshop";
    btn.classList.remove("btn-primary");
    document.querySelector(".subtitle").textContent =
      "FULL DEEP DIVE — 18 steps, all exercises · self-paced or 90-min session";
  }
}

function renderPostEventPanel() {
  const data = state.postEvent;
  const container = $("#post-event-paths");
  if (!data || !container) return;
  let summary = data.summary || "";
  if (data.default_path) {
    summary += ` Default path: ${data.default_path}.`;
  }
  $("#post-event-summary").textContent = summary;
  container.innerHTML = "";
  if (data.champion_path) {
    const champ = document.createElement("p");
    champ.className = "hint champion-path-note";
    champ.innerHTML = `<strong>Champions only:</strong> ${escapeHtml(data.champion_path)}`;
    container.appendChild(champ);
  }
  (data.paths || []).forEach((path) => {
    const div = document.createElement("details");
    div.className = "deep-dive-topic";
    const summary = document.createElement("summary");
    const audience = path.audience ? ` · ${path.audience}` : "";
    summary.textContent = `${path.title} (${path.time})${audience}`;
    div.appendChild(summary);
    const body = document.createElement("div");
    body.className = "deep-dive-body";
    body.innerHTML = `
      <p class="deep-dive-text"><strong>Skipped live:</strong> ${escapeHtml(path.live_cut)}</p>
      <p class="deep-dive-text"><strong>Go to:</strong> <code>${escapeHtml(path.resource)}</code></p>
      <p class="deep-dive-text"><strong>In app:</strong> ${escapeHtml(path.app)}</p>
    `;
    div.appendChild(body);
    container.appendChild(div);
  });
}

async function init() {
  const [health, session, platform, materials, deepDives, postEvent, automation] = await Promise.all([
    api("/health"),
    api("/session"),
    api("/platform-highlights"),
    api("/materials"),
    api("/deep-dives"),
    api("/post-event"),
    api("/automation"),
  ]);

  state.session = session;
  state.platform = platform;
  state.materials = materials;
  state.deepDives = deepDives;
  state.postEvent = postEvent;
  state.automation = automation;
  renderAutomationPanel();
  updateBadges(health);
  startTimer();
  renderApiMatrix();
  renderProductChecklist();

  $("#output-schema").textContent = materials.output_schema;
  $("#opening-script").textContent = materials.opening_script;
  $("#closing-script").textContent = materials.closing_script;
  $("#sample-slack").textContent = materials.sample_slack_review;
  $("#sample-crm").textContent = materials.sample_crm_update;
  $("#sample-outreach").textContent = materials.sample_outreach_draft;

  if (session.connector_map) {
    $("#read-tools").value = session.connector_map.read_tools || "";
    $("#draft-tools").value = session.connector_map.draft_tools || "";
    $("#blocked-tools").value = session.connector_map.blocked || "";
  }
  if (session.company) $("#company").value = session.company;
  if (session.website) $("#website").value = session.website;
  if (session.workflow_goal) $("#workflow-goal").value = session.workflow_goal;
  if (session.job) $("#job").value = session.job;
  if (session.primary_user) $("#primary-user").value = session.primary_user;
  if (session.workflow_owner) $("#workflow-owner").value = session.workflow_owner;
  renderGoalPresets();
  $("#workflow-goal")?.addEventListener("input", syncGoalPresetHighlight);
  if (session.review_status) {
    $("#review-status").value = session.review_status;
  }
  loadPilotForm(session);

  await loadSteps();

  $("#express-toggle").addEventListener("click", async () => {
    state.expressMode = !state.expressMode;
    const url = new URL(window.location.href);
    if (state.expressMode) url.searchParams.delete("full");
    else url.searchParams.set("full", "1");
    url.searchParams.delete("express");
    window.history.replaceState({}, "", url);
    await loadSteps();
  });

  $("#save-inputs-btn").addEventListener("click", saveInputs);
  $("#save-context-btn").addEventListener("click", saveContext);
  $("#load-sample-context-btn").addEventListener("click", () => {
    $("#internal-context").value = materials.sample_internal_context;
  });
  $("#save-connectors-btn").addEventListener("click", saveConnectors);
  $("#save-pilot-btn").addEventListener("click", savePilotPlan);
  $("#review-status").addEventListener("change", saveReviewStatus);
  $("#full-chain-btn").addEventListener("click", runFullChain);
  $("#download-all-btn").addEventListener("click", downloadAllArtifacts);
  $("#download-agent-kit-btn").addEventListener("click", downloadAgentKit);
  $("#download-skill-pack-btn").addEventListener("click", () =>
    downloadHermesSkillPack().catch((e) => alert(e.message))
  );
  $("#copy-install-cmd-btn").addEventListener("click", () =>
    copyText($("#hermes-install-cmd").textContent)
  );
  $("#copy-test-cmd-btn").addEventListener("click", () =>
    copyText($("#hermes-test-cmd").textContent)
  );
  $("#copy-meeting-prep-btn").addEventListener("click", () =>
    copyText($("#meeting-prep-test-cmd").textContent)
  );
  $("#copy-discord-intro-btn").addEventListener("click", () =>
    copyText($("#discord-intro-template").textContent)
  );
  $("#download-community-btn").addEventListener("click", downloadCommunityPlaybook);
  $("#download-pilot-btn").addEventListener("click", downloadPilotTemplate);
  $("#download-champion-rollout-btn")?.addEventListener("click", downloadPilotTemplate);
  $("#copy-broadcast-skill-btn").addEventListener("click", () =>
    copyText($("#broadcast-skill").textContent)
  );
  $("#copy-broadcast-cmd-btn").addEventListener("click", () =>
    copyText($("#broadcast-command").textContent)
  );
  $("#copy-evidence-build-btn").addEventListener("click", () =>
    copyText($("#agent-evidence-bundle").textContent)
  );
  $("#reset-build-progress-btn").addEventListener("click", () => {
    if (!confirm("Reset Agent Build Lab progress?")) return;
    state.buildProgress = {};
    saveBuildProgress();
    renderAgentBuildLab();
  });
  $("#presenter-toggle").addEventListener("click", () => {
    state.presenterMode = !state.presenterMode;
    applyPresenterMode();
  });
  $("#prev-btn").addEventListener("click", () => goToStep(state.currentIndex - 1));
  $("#next-btn").addEventListener("click", () => goToStep(state.currentIndex + 1));
  $("#toggle-raw").addEventListener("click", () => $("#results-raw").classList.toggle("hidden"));
  $("#copy-brief-btn").addEventListener("click", () => copyText($("#brief-content").textContent));
  $("#copy-hermes-btn").addEventListener("click", () => copyText($("#hermes-content").textContent));
  $("#copy-run-command-btn").addEventListener("click", () => copyText($("#hermes-run-command").textContent));
  $("#copy-evidence-btn").addEventListener("click", () => copyText($("#hermes-evidence-bundle").textContent));
  $("#download-card-btn").addEventListener("click", () =>
    downloadMarkdown("account-action-brief-workflow-card.md", $("#card-content").textContent)
  );
  $("#reset-btn").addEventListener("click", async () => {
    if (!confirm("Reset all session data?")) return;
    await api("/session/reset", { method: "POST" });
    location.reload();
  });
}

init().catch((err) => {
  document.body.innerHTML = `<div style="padding:40px;color:#ff6b6b">Failed to load workshop app: ${err.message}</div>`;
});
