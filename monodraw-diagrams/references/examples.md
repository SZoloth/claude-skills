# Complete Diagram Examples

This reference provides full, realistic examples of each diagram type in the Monodraw style.

## System Architecture Examples

### Example 1: E-Commerce Microservices Architecture

This diagram shows a typical e-commerce system with microservices architecture:

```
╔═══════════════════════════════ Cloud Infrastructure ═══════════════════════════════╗
║                                                                                     ║
║  ┌ ─ ─ ─ ─ ─ ─ ─ ─ Frontend ─ ─ ─ ─ ─ ─ ─ ─ ┐                                   ║
║                                                                                     ║
║   ┌───────────┐          ┌───────────┐                                            ║
║  ││    CDN    │         ││   React   │                                            ║
║   │  (Static) │          │    App    │                                            ║
║   └───────────┘          └───────────┘                                            ║
║  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ┘                                           ║
║                             │                                                      ║
║                             ↓                                                      ║
║                      ┌─────────────┐                                               ║
║                      │  API        │                                               ║
║                      │  Gateway    │                                               ║
║                      └─────────────┘                                               ║
║                             │                                                      ║
║         ┌───────────────────┼───────────────────┐                                 ║
║         │                   │                   │                                 ║
║         ↓                   ↓                   ↓                                 ║
║  ┌───────────┐       ┌───────────┐       ┌───────────┐                           ║
║  │   Auth    │       │  Product  │       │   Order   │                           ║
║  │  Service  │       │  Service  │       │  Service  │                           ║
║  └───────────┘       └───────────┘       └───────────┘                           ║
║       │                    │                    │                                 ║
║       │                    │                    │                                 ║
║       ↓                    ↓                    ↓                                 ║
║   ╭───────╮            ╭───────╮            ╭───────╮                             ║
║   │ User  │            │Product│            │ Order │                             ║
║   │  DB   │            │  DB   │            │  DB   │                             ║
║   ╰───────╯            ╰───────╯            ╰───────╯                             ║
║                                                                                     ║
║  ┌ ─ ─ ─ ─ ─ ─ ─ Message Queue ─ ─ ─ ─ ─ ─ ┐                                    ║
║                                                                                     ║
║   ┌─────────────────────────────────┐                                             ║
║  ││       Kafka / RabbitMQ         │                                             ║
║   │         ║│││││││││║             │                                             ║
║   └─────────────────────────────────┘                                             ║
║  └ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ┘                                             ║
║                     │                                                              ║
║                     ↓                                                              ║
║              ┌───────────┐                                                         ║
║              │   Email   │                                                         ║
║              │  Service  │                                                         ║
║              └───────────┘                                                         ║
║                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════╝

Legend:
- Solid arrows (→): Synchronous HTTP requests
- Dashed boxes: Logical groupings
- Double-line box: External boundary
- Cylinders (╭─╮): Databases
```

### Example 2: Authentication Flow

This diagram illustrates OAuth2 authentication flow:

```
┌──────────┐                                        ┌──────────┐
│  Client  │                                        │   Auth   │
│   App    │                                        │  Server  │
└──────────┘                                        └──────────┘
     │                                                    │
     │ 1. Request authorization                          │
     │ ─────────────────────────────────────────────────→│
     │                                                    │
     │                    2. Authorization prompt        │
     │←─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │
     │                                                    │
     │ 3. User approves                                  │
     │ ─────────────────────────────────────────────────→│
     │                                                    │
     │                    4. Authorization code          │
     │←──────────────────────────────────────────────────│
     │                                                    │
     │ 5. Exchange code for token                        │
     │ ─────────────────────────────────────────────────→│
     │                                                    │
     │                    6. Access token                │
     │←══════════════════════════════════════════════════│
     │                                                    │
     ↓                                                    ↓
┌──────────┐                                        ┌──────────┐
│ API Call │                                        │ Resource │
│with token│ ─────────────────────────────────────→ │  Server  │
└──────────┘         7. Access resource             └──────────┘

Legend:
- Solid arrows (→): HTTP requests
- Dashed arrows (⇢): Redirects
- Double arrows (⇒): Secure token transfer
```

## Workflow Process Examples

### Example 3: Order Processing Workflow

This diagram shows an e-commerce order processing workflow with decision points:

```
╭──────────╮
│  START   │
│New Order │
╰──────────╯
     │
     ↓
┌──────────────┐
│ Validate     │
│ Order Data   │
└──────────────┘
     │
     ↓
    ╱╲
   ╱  ╲
  ╱Valid╲
  ╲  ?  ╱
   ╲  ╱
    ╲╱
   │  │
 No│  │Yes
   │  │
   ↓  └──────────────┐
┌──────────┐         │
│ Return   │         ↓
│  Error   │    ┌──────────────┐
└──────────┘    │ Check        │
   │            │ Inventory    │
   │            └──────────────┘
   │                 │
   │                 ↓
   │                ╱╲
   │               ╱  ╲
   │              ╱ In  ╲
   │              ╲Stock╱
   │               ╲  ╱
   │                ╲╱
   │               │  │
   │             No│  │Yes
   │               │  │
   │               ↓  └──────────────┐
   │          ┌──────────┐           │
   │          │ Backorder│           ↓
   │          │  Item    │      ┌──────────────┐
   │          └──────────┘      │ Reserve      │
   │               │            │ Inventory    │
   │               │            └──────────────┘
   │               │                 │
   │               └────────┬────────┘
   │                        ↓
   │                   ┌──────────────┐
   │                   │ Process      │
   │                   │ Payment      │
   │                   └──────────────┘
   │                        │
   │                        ↓
   │                       ╱╲
   │                      ╱  ╲
   │                     ╱ Pay ╲
   │                     ╲ OK? ╱
   │                      ╲  ╱
   │                       ╲╱
   │                      │  │
   │                    No│  │Yes
   │                      │  │
   │                      ↓  └──────────────┐
   │                 ┌──────────┐           │
   │                 │ Cancel   │           ↓
   │                 │  Order   │      ┌──────────────┐
   │                 └──────────┘      │ Fulfill      │
   │                      │            │ Order        │
   │                      │            └──────────────┘
   │                      │                 │
   └──────────────────────┴─────────────────┘
                          │
                          ↓
                    ╭──────────╮
                    │   END    │
                    │  Notify  │
                    │ Customer │
                    ╰──────────╯
```

### Example 4: Swim Lane - Customer Support Process

This diagram shows a customer support workflow across different actors:

```
┌────────────────────────────────────────────────────────────────────────────────┐
│ Customer        │ Submit Ticket │        │  Receive    │                       │
│                 │               │        │  Response   │                       │
├────────────────────────────────────────────────────────────────────────────────┤
│ Support         │               │ Triage │             │  Respond   │          │
│ Agent           │               │ Ticket │             │  to        │          │
│                 │               │        │             │ Customer   │          │
├────────────────────────────────────────────────────────────────────────────────┤
│ System          │  Create       │ Route  │  Escalate?  │            │  Close   │
│                 │  in CRM       │ to     │             │            │  Ticket  │
│                 │               │ Agent  │             │            │          │
├────────────────────────────────────────────────────────────────────────────────┤
│ Engineering     │               │        │   Yes ──→   │ Investigate│          │
│ Team            │               │        │   Fix Bug   │            │          │
└────────────────────────────────────────────────────────────────────────────────┘
                 Time ──────────────────────────────────────────→
```

## System Map Examples (Donella Meadows Style)

### Example 5: Product Growth Loop

This diagram shows reinforcing and balancing loops in product growth:

```
                              (+)
                    ┌──────────────────────┐
                    │                      ↓
                ┌────────┐            ┌────────┐
          ┌────→│ Users  │            │Revenue │
          │     └────────┘            └────────┘
          │         │                      │
          │         │                      │
          │      (+)│                      │(+)
          │         ↓                      ↓
          │    ┌────────┐            ┌────────┐
          │    │ Value  │            │ R & D  │
          │    │Created │            │Spending│
          │    └────────┘            └────────┘
          │         │                      │
          │         │                      │
          │      (+)│                      │(+)
          │         ↓                      ↓
          │    ┌─────────────────────────────┐
          │    │    Product Quality          │
          │    └─────────────────────────────┘
          │                  │
          │               (+)│
          └──────────────────┘

                R1: Network Effect
                R2: Quality Loop


                 Growth Constraints:

                 ┌────────┐
                 │ Costs  │
                 └────────┘
                      │
                   (-)│
                      ↓
                 ┌────────┐
                 │Revenue │
                 └────────┘
                      ↑
                   (+)│
                      │
                 ┌────────┐
                 │ Users  │
                 └────────┘

                B1: Cost Pressure
```

### Example 6: Coffee Temperature System

This diagram shows a classic balancing loop with delay:

```
                    (+)
           ┌─────────────────┐
           │                 ↓
      ┌────────┐        ┌────────┐
      │ Actual │        │  Gap   │
      │  Temp  │        │        │
      └────────┘        └────────┘
           ↑                 │
           │                 │
           │                 │(+)
           │                 ↓
           │            ┌────────┐
           │            │ Heating│
           │            │  Rate  │
           │            └────────┘
           │                 │
           │                 │
           │     (+)         │
           │──────||─────────┘
                 Delay

        B1: Temperature Control
        (Thermostat)

        Goal Temperature: 160°F
```

### Example 7: Stock and Flow - Inventory System

This diagram shows stock and flow notation:

```
                Orders
    ~~~~~  ─────>◁─────→  ┌─────────────┐  ─────>◁─────→  ~~~~~
   Supply               │  Inventory  │               Sales
                          └─────────────┘
                                │
                                │
                                ↓
                          ┌─────────────┐
                          │   Reorder   │
                          │    Point    │
                          └─────────────┘
                                │
                                │(+)
                   ┌────────────┘
                   │
                   │                 (-)
                   ↓       ┌──────────────────┐
              ┌────────┐   │                  ↓
              │ Order  │   │             ┌────────┐
              │ Signal │   │             │ Lead   │
              └────────┘   │             │ Time   │
                   │       │             └────────┘
                (+)│       │                  │
                   │       │                  │──||──→ Delay
                   ↓       │                        │
    ~~~~~  ←───────┘       └────────────────────────┘

    B1: Inventory Control Loop
    || = Processing and shipping delay
```

## Service Blueprint Examples

### Example 8: Restaurant Service Blueprint

This diagram shows the complete customer journey through a restaurant:

```
─────────────────────────────────────────────────────────────────────────────────
  Customer Actions
─────────────────────────────────────────────────────────────────────────────────
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Arrive  │ ─→ │   Seat   │ ─→ │  Order   │ ─→ │   Eat    │ ─→ │   Pay    │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
═════════════════════════════════════════════════════════════════════════════════
  Line of Interaction
─────────────────────────────────────────────────────────────────────────────────
  Frontstage (Visible to Customer)
─────────────────────────────────────────────────────────────────────────────────
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Greet   │    │  Guide   │    │   Take   │    │  Serve   │    │ Process  │
  │ Customer │    │ to Table │    │  Order   │    │   Food   │    │ Payment  │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
                                        │               ↑               │
                                        ↓               │               ↓
═════════════════════════════════════════════════════════════════════════════════
  Line of Visibility
─────────────────────────────────────────────────────────────────────────────────
  Backstage (Invisible to Customer)
─────────────────────────────────────────────────────────────────────────────────
                  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
                  │  Check   │    │  Relay   │    │ Prepare  │    │  Update  │
                  │  Table   │    │ Order to │    │   Food   │    │ Billing  │
                  │Available │    │ Kitchen  │    │          │    │  System  │
                  └──────────┘    └──────────┘    └──────────┘    └──────────┘
                       │               │               │               │
                       ↓               ↓               ↓               ↓
═════════════════════════════════════════════════════════════════════════════════
  Internal Interaction Line
─────────────────────────────────────────────────────────────────────────────────
  Support Processes
─────────────────────────────────────────────────────────────────────────────────
                  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
                  │  Table   │    │ Kitchen  │    │Inventory │    │   POS    │
                  │  Mgmt    │    │ Display  │    │  System  │    │  System  │
                  │  System  │    │  System  │    │          │    │          │
                  └──────────┘    └──────────┘    └──────────┘    └──────────┘
─────────────────────────────────────────────────────────────────────────────────
                             Time ──────────────────────→

Pain Points:
⚠ Long wait during busy hours (between Arrive and Seat)
⚠ Kitchen delays during peak times (between Order and Serve)
```

### Example 9: Digital Product Onboarding

This diagram maps user onboarding for a SaaS product:

```
─────────────────────────────────────────────────────────────────────────────────
  User Journey
─────────────────────────────────────────────────────────────────────────────────
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Sign    │ ─→ │  Verify  │ ─→ │  Setup   │ ─→ │   Use    │ ─→ │ Upgrade  │
  │   Up     │    │  Email   │    │ Profile  │    │  Product │    │   Plan   │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
═════════════════════════════════════════════════════════════════════════════════
  Line of Interaction
─────────────────────────────────────────────────────────────────────────────────
  Frontend (UI)
─────────────────────────────────────────────────────────────────────────────────
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Form    │    │  Email   │    │  Guided  │    │Dashboard │    │ Pricing  │
  │  Page    │    │  Prompt  │    │  Tour    │    │   View   │    │   Page   │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
       │               │               │               │               │
       ↓               ↓               ↓               ↓               ↓
═════════════════════════════════════════════════════════════════════════════════
  Line of Visibility
─────────────────────────────────────────────────────────────────────────────────
  Backend Services
─────────────────────────────────────────────────────────────────────────────────
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Create  │    │   Send   │    │  Track   │    │  Log     │    │ Process  │
  │ Account  │    │Verify    │    │  Tour    │    │ Activity │    │ Payment  │
  │          │    │  Link    │    │Progress  │    │          │    │          │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
       │               │               │               │               │
       ↓               ↓               ↓               ↓               ↓
═════════════════════════════════════════════════════════════════════════════════
  Support Infrastructure
─────────────────────────────────────────────────────────────────────────────────
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │   User   │    │  Email   │    │Analytics │    │   Event  │    │ Payment  │
  │  Database│    │ Service  │    │  System  │    │ Tracking │    │ Gateway  │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
─────────────────────────────────────────────────────────────────────────────────
                             Time ──────────────────────→

Touchpoints:
✓ Welcome email (after Sign Up)
✓ Verification email (after Verify Email)
✓ Onboarding email sequence (during Setup and Use)
⚠ Drop-off point: 40% abandon at Email verification
```

## Mixed/Complex Examples

### Example 10: LLM Thread Referencing (from original image)

This diagram shows how a second model extracts information from a previous thread:

```
                            Referencing threads


┌────────────────────────────────────────────────────────────────────────────┐
│                                                                            │
│  ┌──────────────────────────────────────────────────────────┐             │
│  │                                                           │             │
│  │  User: Implement the plan we discussed in thread T-1234. │             │
│  │                                                           │             │
│  └──────────────────────────────────────────────────────────┘             │
│                                                                            │
│       ┌──────────────────────────────┐                                    │
│       │ Model: Let me read that thread                                    │
│       └──────────────────────────────┘                                    │
│                                                                            │
│       ┌──────────────────────────────┐                                    │
│       │ Tool Call: read_thread({      │                                    │
│       │   thread_id: T-1234          │                                    │
│       │   goal: "Extract the plan"   │──────────────┐                     │
│       │ })                           │              │                     │
│       └──────────────────────────────┘              │                     │
│                                                      │                     │
│                                                      │                     │
│  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ┐  │
│                                                      │                     │
│  │   1. A second model is tasked with extracting    │                  │  │
│       the relevant information from the thread.      │                     │
│  │                                                   ↓                  │  │
│                                                                            │
│  │              ┌─────────────────────────────────────────────┐        │  │
│                 │ Model 1: Read this thread and extract the   │           │
│  │              │          plan.                              │        │  │
│                 │                                             │           │
│  │              │ <contents of thread T-1234>                 │        │  │
│                 │                                             │           │
│  │              └─────────────────────────────────────────────┘        │  │
│                                    │                                      │
│  │                                 │                                   │  │
│                                    ↓                                      │
│  │              ┌─────────────────────────────────────────────┐        │  │
│                 │ Model 2: Here is the plan:                  │           │
│  │              │                                             │        │  │
│                 │ [plan extracted from T-1234]                │           │
│  │              │                                             │        │  │
│                 └─────────────────────────────────────────────┘           │
│  │                                 │                                   │  │
│                                    │                                      │
│  │   2. The response of the second model is returned           │  │     │
│                                    │                                      │
│  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘  │
│                                    │                                      │
│                                    │                                      │
│       ┌──────────────────────────────────────────────────────┐           │
│       │ Tool Call Result: "Here is the plan from             │           │
│   ────┤ T-1234: [plan]"                                      │           │
│       └──────────────────────────────────────────────────────┘           │
│                                                                            │
│       ┌──────────────────────────────┐                                    │
│       │ Model: I see. Let's implement it.                                 │
│       └──────────────────────────────┘                                    │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

### Example 11: Doubly Linked List (from original image)

This diagram shows a classic data structure:

```


  ┌──────┐
  │ head │                                                              ┌──────┐
  └──────┘                                                              │ tail │
     ││·····                                                              └──────┘
     ││····│·                                                              ··││
  ┌──↓↓────↓──┐  ·····                                         ·····   ┌──↑↑────↑──┐
  │          │··    ·│                                        │·    ··  │          │
  │  node 1  │·  ┌───↓────┐  ·····              ·····   ┌────↓───┐  · │  node 4  │
  │          │···│        │··    ·│            │·    ··  │        │···│          │
  └──────────┘  ·│ node 2 │·  ┌───↓────┐ ┌────↓───┐  · │ node 3 │  · └──────────┘
     ││·····    ·│        │···│        │·│        │···│        │·    ·····││
     ││····│·   ·└────────┘  ·│ node 3 │·│ node 2 │·  └────────┘   ·│····││
     ││···········    ││·····→│        │←│        │←·····││    ···········││
     ││··········│·   ││····│·└────────┘·└────────┘·│····││   ·│··········││
     ↓↓          ↓    ↓↓    ↓           ·          ↓    ↓↓    ↓          ↓↓
  ┌──────────┐     ┌──────────┐       ┌──────────┐     ┌──────────┐  ┌──────────┐
  │   data   │     │   data   │       │   data   │     │   data   │  │   data   │
  └──────────┘     └──────────┘       └──────────┘     └──────────┘  └──────────┘


```

Note: This example uses the dotted/stippled effect (·) to show the pointers connecting nodes.

## Tips for Creating These Diagrams

1. **Start with the skeleton** - lay out boxes and primary flow first
2. **Add connections** - draw arrows showing relationships
3. **Add labels** - clearly name each component
4. **Add grouping** - use dashed boxes for logical boundaries
5. **Add emphasis** - use stippling or shading for important areas
6. **Add legend** - explain symbols and arrow types
7. **Review alignment** - ensure everything sits on a consistent grid
8. **Test readability** - view in monospaced font to check clarity
