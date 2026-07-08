# Source Notes

These notes were used to keep the workshop copy accurate as of June 21, 2026.

- You.com docs describe the platform as real-time web intelligence for agentic apps, with Search, Content/Contents, and Research APIs: https://you.com/docs/welcome
- The Search API returns structured, LLM-optimized web and news results with snippets, metadata, optional live crawl, domain controls, freshness controls, and JSON output: https://you.com/docs/guides/search
- The Contents API extracts clean HTML or Markdown content from specific webpages on demand: https://you.com/docs/guides/contents
- The Research API supports synthesized research outputs and source controls such as included domains, freshness, country, and structured output: https://you.com/docs/guides/research
- You.com documents an MCP server for web search at `https://api.you.com/mcp`, including a free search profile and paid access to additional tools: https://you.com/docs/capabilities/mcp-server-for-web-search
- You.com citation-grounding guidance describes a minimal loop: call Search API, format snippets as context, prompt the LLM with citation instructions, and render response plus source list: https://you.com/docs/capabilities/grounding-llm-responses-with-citations
- The conversion-focused version treats CRM, Slack/Teams, docs, meeting intelligence, outreach, support, analytics, project trackers, and governance systems as integration patterns. Specific connector availability should be validated before making hard implementation claims.

Positioning caveat:

The workshop brief refers to You.com's upcoming Answers API. Public You.com docs currently emphasize Search, Contents, Research, Finance Research, MCP, and citation grounding, so this content treats Answers API as an upcoming product area and includes feedback capture rather than public-doc claims.

Hermes caveat:

The Hermes governance language in this pack is based on the provided workshop brief, not independently verified public docs.

NemoClaw caveat:

I could not find reliable public NemoClaw product documentation during web research on June 21, 2026. NemoClaw integration content is therefore positioned as a capability-based legal, compliance, policy, approved-language, or capability-governance review layer that should be validated against actual NemoClaw capabilities before publishing.
