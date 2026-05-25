import * as params from '@params';

const resList = document.getElementById('searchResults');
const sInput = document.getElementById('searchInput');
const searchBox = document.getElementById('searchbox');
const searchStatus = document.getElementById('searchStatus');

let fuse;
let currentElement = null;
let firstResult = null;
let lastResult = null;
let activeQuery = '';

const defaultFuseOptions = {
    distance: 100,
    threshold: 0.34,
    ignoreLocation: true,
    includeMatches: true,
    includeScore: true,
    keys: [
        { name: 'title', weight: 0.45 },
        { name: 'summary', weight: 0.25 },
        { name: 'tags', weight: 0.15 },
        { name: 'categories', weight: 0.1 },
        { name: 'content', weight: 0.05 }
    ]
};

const buildFuseOptions = () => {
    if (!params.fuseOpts) {
        return defaultFuseOptions;
    }

    return {
        isCaseSensitive: params.fuseOpts.iscasesensitive ?? false,
        includeScore: params.fuseOpts.includescore ?? false,
        includeMatches: true,
        minMatchCharLength: params.fuseOpts.minmatchcharlength ?? 1,
        shouldSort: params.fuseOpts.shouldsort ?? true,
        findAllMatches: params.fuseOpts.findallmatches ?? false,
        keys: params.fuseOpts.keys ?? defaultFuseOptions.keys,
        location: params.fuseOpts.location ?? 0,
        threshold: params.fuseOpts.threshold ?? defaultFuseOptions.threshold,
        distance: params.fuseOpts.distance ?? defaultFuseOptions.distance,
        ignoreLocation: params.fuseOpts.ignorelocation ?? defaultFuseOptions.ignoreLocation
    };
};

const debounce = (fn, delay) => {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = window.setTimeout(() => fn(...args), delay);
    };
};

const escapeHtml = (value = '') => value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');

const escapeRegExp = (value = '') => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

const highlightText = (value = '', query = '') => {
    const cleaned = query.trim();
    if (!cleaned) {
        return escapeHtml(value);
    }

    const terms = [...new Set(cleaned.split(/\s+/).filter(Boolean))];
    if (!terms.length) {
        return escapeHtml(value);
    }

    const pattern = terms.map((term) => escapeRegExp(term)).join('|');
    const regex = new RegExp(`(${pattern})`, 'gi');
    return escapeHtml(value).replace(regex, '<mark>$1</mark>');
};

const buildSnippet = (item, query) => {
    const source = item.summary || item.content || '';
    const cleanedSource = source.replace(/\s+/g, ' ').trim();
    if (!cleanedSource) {
        return '';
    }

    const normalizedQuery = query.trim().toLowerCase();
    const index = normalizedQuery ? cleanedSource.toLowerCase().indexOf(normalizedQuery) : -1;
    const snippet = index >= 0
        ? cleanedSource.slice(Math.max(0, index - 60), index + normalizedQuery.length + 120)
        : cleanedSource.slice(0, 180);

    return `${highlightText(snippet, query)}${cleanedSource.length > snippet.length ? '…' : ''}`;
};

const formatSectionLabel = (item) => {
    if (item.section === 'notes') {
        return item.lang === 'vi' ? 'Ghi chú' : 'Note';
    }

    return item.lang === 'vi' ? 'Bài viết' : 'Post';
};

const rankResults = (results, query) => {
    const normalizedQuery = query.trim().toLowerCase();
    return [...results].sort((left, right) => {
        const leftTitle = left.item.title.toLowerCase();
        const rightTitle = right.item.title.toLowerCase();
        const leftTags = (left.item.tags || []).map((tag) => String(tag).toLowerCase());
        const rightTags = (right.item.tags || []).map((tag) => String(tag).toLowerCase());
        const leftExact = leftTitle === normalizedQuery ? 1 : 0;
        const rightExact = rightTitle === normalizedQuery ? 1 : 0;
        const leftPrefix = leftTitle.startsWith(normalizedQuery) ? 1 : 0;
        const rightPrefix = rightTitle.startsWith(normalizedQuery) ? 1 : 0;
        const leftTagHit = leftTags.includes(normalizedQuery) ? 1 : 0;
        const rightTagHit = rightTags.includes(normalizedQuery) ? 1 : 0;

        if (leftExact !== rightExact) {
            return rightExact - leftExact;
        }
        if (leftPrefix !== rightPrefix) {
            return rightPrefix - leftPrefix;
        }
        if (leftTagHit !== rightTagHit) {
            return rightTagHit - leftTagHit;
        }

        return (left.score ?? 0) - (right.score ?? 0);
    });
};

const updateStatus = (message) => {
    if (!searchStatus) {
        return;
    }

    searchStatus.innerHTML = message;
};

const announceResults = (query, count) => {
    const emptyLabel = searchBox?.dataset.emptyLabel ?? 'No results yet.';
    const singularLabel = searchBox?.dataset.oneLabel ?? '1 result';
    const pluralLabel = searchBox?.dataset.manyLabel ?? '{{count}} results';

    if (!query) {
        updateStatus(emptyLabel);
        return;
    }

    if (count === 0) {
        updateStatus(highlightText(emptyLabel.replace('{{query}}', query), query));
        return;
    }

    const label = count === 1 ? singularLabel : pluralLabel.replace('{{count}}', `${count}`);
    updateStatus(`${label} <span class="search-hint">${searchBox?.dataset.hintLabel ?? ''}</span>`);
};

const dispatchSearchEvent = (count) => {
    document.dispatchEvent(new CustomEvent('search:rendered', {
        detail: {
            count,
            query: activeQuery
        }
    }));
};

const resetState = () => {
    currentElement = null;
    firstResult = null;
    lastResult = null;
};

const reset = () => {
    resetState();
    resList.innerHTML = '';
    sInput.value = '';
    activeQuery = '';
    announceResults('', 0);
    dispatchSearchEvent(0);
    sInput.focus();
};

const setActiveResult = (element) => {
    document.querySelectorAll('.searchResults .focus').forEach((item) => item.classList.remove('focus'));

    if (!element) {
        return;
    }

    element.focus();
    element.parentElement?.classList.add('focus');
    currentElement = element;
};

const renderResults = (results) => {
    if (!Array.isArray(results) || results.length === 0) {
        resList.innerHTML = '';
        resetState();
        announceResults(activeQuery, 0);
        dispatchSearchEvent(0);
        return;
    }

    const fragment = document.createDocumentFragment();

    for (const result of results) {
        const item = result.item;
        const li = document.createElement('li');
        li.className = 'search-result-item';

        const link = document.createElement('a');
        link.className = 'entry-link';
        link.href = item.permalink;
        link.setAttribute('aria-label', item.title);
        link.dataset.searchQuery = activeQuery;

        const title = document.createElement('span');
        title.className = 'search-result-title';
        title.innerHTML = highlightText(item.title, activeQuery);

        const meta = document.createElement('span');
        meta.className = 'search-result-meta';
        meta.textContent = `${formatSectionLabel(item)} · ${new URL(item.permalink).pathname}`;

        const snippet = document.createElement('span');
        snippet.className = 'search-result-snippet';
        snippet.innerHTML = buildSnippet(item, activeQuery);

        link.appendChild(title);
        link.appendChild(meta);
        if (snippet.innerHTML) {
            link.appendChild(snippet);
        }
        li.appendChild(link);
        fragment.appendChild(li);
    }

    resList.innerHTML = '';
    resList.appendChild(fragment);
    firstResult = resList.firstElementChild;
    lastResult = resList.lastElementChild;
    announceResults(activeQuery, results.length);
    dispatchSearchEvent(results.length);
};

const performSearch = () => {
    if (!fuse) {
        return;
    }

    const query = sInput.value.trim();
    activeQuery = query;
    if (!query) {
        renderResults([]);
        return;
    }

    const searchOptions = params.fuseOpts?.limit ? { limit: params.fuseOpts.limit } : undefined;
    const results = searchOptions ? fuse.search(query, searchOptions) : fuse.search(query);
    renderResults(rankResults(results, query));
};

const initSearch = async () => {
    if (!sInput || !resList) {
        return;
    }

    sInput.disabled = false;
    sInput.focus();
    announceResults('', 0);

    try {
        const response = await fetch('../index.json');
        if (!response.ok) {
            throw new Error(`Search index load failed: ${response.status}`);
        }

        const data = await response.json();
        if (data) {
            fuse = new Fuse(data, buildFuseOptions());
        }
    } catch (error) {
        console.error(error);
        updateStatus(searchBox?.dataset.errorLabel ?? 'Search index could not be loaded.');
    }
};

window.addEventListener('load', initSearch);

sInput?.addEventListener('input', debounce(performSearch, 120));

sInput?.addEventListener('search', () => {
    if (!sInput.value) {
        reset();
    }
});

resList?.addEventListener('click', (event) => {
    const link = event.target.closest('.entry-link');
    if (!link) {
        return;
    }

    document.dispatchEvent(new CustomEvent('search:result-click', {
        detail: {
            query: link.dataset.searchQuery || '',
            href: link.href,
            title: link.querySelector('.search-result-title')?.textContent?.trim() || ''
        }
    }));
});

document.addEventListener('keydown', (event) => {
    const { key } = event;
    const active = document.activeElement;
    const isInSearchBox = searchBox?.contains(active);

    if (key === 'Escape') {
        reset();
        return;
    }

    if (key === 'Enter' && active === sInput && firstResult) {
        event.preventDefault();
        firstResult.querySelector('.entry-link')?.click();
        return;
    }

    if (!firstResult || !isInSearchBox) {
        return;
    }

    if (key === 'ArrowDown') {
        event.preventDefault();

        if (active === sInput) {
            setActiveResult(firstResult.querySelector('.entry-link'));
        } else if (active?.parentElement !== lastResult) {
            setActiveResult(active?.parentElement?.nextElementSibling?.querySelector('.entry-link'));
        }
    } else if (key === 'ArrowUp') {
        event.preventDefault();

        if (active?.parentElement === firstResult) {
            setActiveResult(sInput);
        } else if (active !== sInput) {
            setActiveResult(active?.parentElement?.previousElementSibling?.querySelector('.entry-link'));
        }
    } else if (key === 'ArrowRight') {
        if (active?.matches?.('.entry-link')) {
            active.click();
        }
    }
});
