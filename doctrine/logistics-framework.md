# Logistics Framework

The flagship reference implementation is governed by a shipping-and-receiving logistics model.

## Canonical doctrine

> **Data is cargo. Humans are senders and receivers. Agents are couriers. Models are freight. Verification is proof of delivery.**

The framework no longer treats the operator as traveling through a meaning-space. The system handles packages: information is prepared, classified, routed, transported, received, checked, and released.

## Four-function control spine

> **LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY**

### 1. Location
Identify the proposition, package, route context, and handling destination.

### 2. Accounting
Record what the package contains, where it came from, what supports it, what remains unknown, and what dependencies it carries.

### 3. Adjudication
Compare the delivered package against the relevant warrant, evidence, comparator, or ground-truth fixture. Routing and accounting do not themselves establish truth.

### 4. Authority
Release occurs only under valid human authority. Agents, models, routing layers, and transport systems may classify, account, route, hold, compare, and report; they do not possess final release authority.

## Logistics roles

- **Sender** — originates a package or request.
- **Receiver / consignee** — intended recipient and release context.
- **Courier / agent** — transports or transforms a package under declared instructions.
- **Freight / model service** — computational capability used during transport or handling.
- **Shipping & Receiving Control Desk** — human command, handling, and release authority.
- **D.A.T.A. Connector** — Direct / Anchor / Throttle / Audit execution interface.
- **Verification Tag** — proof-of-delivery metadata and status.
- **Claim Comparator** — comparison fixture for adjudication.
- **Consignee Release Latch** — explicit human release control.

## Canonical Verification Tag

The six controlled fields are:

- `RUN_ID`
- `CARGO_CLASS`
- `QUALIFICATION_ID`
- `ROUTE_PLAN_ID`
- `STATUS`
- `ELAPSED_TIME`

Controlled `STATUS` values:

- `HELD`
- `VERIFIED`
- `RELEASED`
- `BLOCKED`

**UI STATE ≠ VERIFICATION TAG STATUS.**

## Semantic firewall

Epistemic control may classify, account, route, and hold. Verification may compare and adjudicate. Human authority alone releases.

The following are prohibited in the current flagship vocabulary and visual system: aircraft, cockpit, runway, airspace, aviation-control imagery, travel-through-meaning-space metaphors, and any predecessor product name tied to that theme.
